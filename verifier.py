from graph import Graph
from LTL import LTLFormula, LTLOperator

class LTLVerifier:

    def __init__(self, graph: Graph):
        self.graph = graph

    def evaluate(self, formula: LTLFormula, state_name: str, visited=None):
        if visited is None:
            visited = set()

        state = self.graph.states[state_name]

        # proposition
        if formula.proposition:
            return any(p.name == formula.proposition.name for p in state.propositions)

        op = formula.operator

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
            neighbors = self.graph.neighbors(state_name)
            return any(self.evaluate(formula.left, n.name) for n in neighbors)

        # EVENTUALLY (F)
        if op == LTLOperator.EVENTUALLY:
            if state_name in visited:
                return False

            visited.add(state_name)

            if self.evaluate(formula.left, state_name):
                return True

            neighbors = self.graph.neighbors(state_name)
            return any(self.evaluate(formula, n.name, visited) for n in neighbors)

        # ALWAYS (G)
        if op == LTLOperator.ALWAYS:
            if state_name in visited:
                return True

            visited.add(state_name)

            if not self.evaluate(formula.left, state_name):
                return False

            neighbors = self.graph.neighbors(state_name)
            return all(self.evaluate(formula, n.name, visited) for n in neighbors)

        # UNTIL (U)
        if op == LTLOperator.UNTIL:
            if self.evaluate(formula.right, state_name):
                return True

            if not self.evaluate(formula.left, state_name):
                return False

            neighbors = self.graph.neighbors(state_name)
            return any(self.evaluate(formula, n.name, visited) for n in neighbors)

        return False
