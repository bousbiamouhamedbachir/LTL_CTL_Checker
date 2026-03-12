from LTL import LTLFormula, LTLOperator
from CTL import CTLFormula, CTLOperator

class LTLVerifier:

    def __init__(self, graph):
        self.graph = graph

    def evaluate(self, formula: LTLFormula, state_name: str, visited=None):
        if visited is None:
            visited = set()

        state = self.graph.states[state_name]

        # Atomic proposition
        if formula.proposition:
            return any(p.name == formula.proposition.name for p in state.propositions)

        op = formula.operator

        neighbors = self.graph.neighbors(state_name)

        # NOT
        if op == LTLOperator.NOT:
            return not self.evaluate(formula.left, state_name, visited)

        # AND
        if op == LTLOperator.AND:
            return self.evaluate(formula.left, state_name, visited) and \
                   self.evaluate(formula.right, state_name, visited)

        # OR
        if op == LTLOperator.OR:
            return self.evaluate(formula.left, state_name, visited) or \
                   self.evaluate(formula.right, state_name, visited)

        # NEXT (X)
        if op == LTLOperator.NEXT:
            return any(self.evaluate(formula.left, n.name) for n in neighbors)

        # EVENTUALLY (F)
        if op == LTLOperator.EVENTUALLY:
            if state_name in visited:
                return False
            visited.add(state_name)
            if self.evaluate(formula.left, state_name):
                return True
            return any(self.evaluate(formula, n.name, visited) for n in neighbors)

        # ALWAYS (G)
        if op == LTLOperator.ALWAYS:
            if state_name in visited:
                return True
            visited.add(state_name)
            if not self.evaluate(formula.left, state_name):
                return False
            return all(self.evaluate(formula, n.name, visited) for n in neighbors)

        # UNTIL (U)
        if op == LTLOperator.UNTIL:
            if self.evaluate(formula.right, state_name):
                return True
            if not self.evaluate(formula.left, state_name):
                return False
            return any(self.evaluate(formula, n.name, visited) for n in neighbors)

        return False


class CTLVerifier:

    def __init__(self, graph):
        self.graph = graph

    def evaluate(self, formula: CTLFormula, state_name: str, visited=None):
        if visited is None:
            visited = set()

        state = self.graph.states[state_name]
        neighbors = self.graph.neighbors(state_name)

        # Atomic proposition
        if formula.proposition:
            return any(p.name == formula.proposition.name for p in state.propositions)

        op = formula.operator

        # NOT
        if op == CTLOperator.NOT:
            return not self.evaluate(formula.left, state_name, visited.copy())

        # AND
        if op == CTLOperator.AND:
            return self.evaluate(formula.left, state_name, visited.copy()) and \
                   self.evaluate(formula.right, state_name, visited.copy())

        # OR
        if op == CTLOperator.OR:
            return self.evaluate(formula.left, state_name, visited.copy()) or \
                   self.evaluate(formula.right, state_name, visited.copy())

        # EX: exists next
        if op == CTLOperator.EX:
            return any(self.evaluate(formula.left, n.name, set()) for n in neighbors)

        # AX: all next
        if op == CTLOperator.AX:
            return all(self.evaluate(formula.left, n.name, set()) for n in neighbors)

        # EF: exists eventually
        if op == CTLOperator.EF:
            if state_name in visited:
                return False
            visited.add(state_name)
            if self.evaluate(formula.left, state_name, visited.copy()):
                return True
            return any(self.evaluate(formula, n.name, visited.copy()) for n in neighbors)

        # AF: all eventually
        if op == CTLOperator.AF:
            if state_name in visited:
                return True
            visited.add(state_name)
            if self.evaluate(formula.left, state_name, visited.copy()):
                return True
            return all(self.evaluate(formula, n.name, visited.copy()) for n in neighbors)

        # EG: exists globally
        if op == CTLOperator.EG:
            if state_name in visited:
                return True
            visited.add(state_name)
            if not self.evaluate(formula.left, state_name, visited.copy()):
                return False
            return any(self.evaluate(formula, n.name, visited.copy()) for n in neighbors)

        # AG: all globally
        if op == CTLOperator.AG:
            if state_name in visited:
                return True
            visited.add(state_name)
            if not self.evaluate(formula.left, state_name, visited.copy()):
                return False
            return all(self.evaluate(formula, n.name, visited.copy()) for n in neighbors)

        # AU: all until
        if op == CTLOperator.AU:
            if state_name in visited:
                return True
            visited.add(state_name)
            if self.evaluate(formula.right, state_name, visited.copy()):
                return True
            if not self.evaluate(formula.left, state_name, visited.copy()):
                return False
            return all(self.evaluate(formula, n.name, visited.copy()) for n in neighbors)

        # EU: exists until
        if op == CTLOperator.EU:
            if state_name in visited:
                return False
            visited.add(state_name)
            if self.evaluate(formula.right, state_name, visited.copy()):
                return True
            if not self.evaluate(formula.left, state_name, visited.copy()):
                return False
            return any(self.evaluate(formula, n.name, visited.copy()) for n in neighbors)

        return False

class Switcher:

    def __init__(self, graph):
        self.graph = graph
        self.logic = None
        self.verifier = None

    def set_logic(self, logic_type: str):
        if logic_type.lower() == "ltl":
            self.logic = "LTL"
            self.verifier = LTLVerifier(self.graph)
        elif logic_type.lower() == "ctl":
            self.logic = "CTL"
            self.verifier = CTLVerifier(self.graph)
        else:
            raise ValueError("Logic type must be 'LTL' or 'CTL'")

    def evaluate(self, formula, state_name):
        if not self.verifier:
            raise ValueError("Logic not set. Call set_logic() first.")
        return self.verifier.evaluate(formula, state_name)
