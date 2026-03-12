import json
from proposition import Proposition
from state import State
from graph import Graph
from LTL import LTLFormula, LTLOperator


def load_graph(filename: str) -> Graph:
    with open(filename) as f:
        data = json.load(f)

    g = Graph()

    # create states
    for s in data["states"]:
        props = [Proposition(p) for p in s["props"]]
        state = State(s["name"], props)
        g.add_state(state)

    # create arcs
    for a in data["arcs"]:
        g.add_arc(a[0], a[1])

    return g



def tokenize(text: str):
    symbols = ['(', ')', '!', '&', '|']
    for s in symbols:
        text = text.replace(s, f' {s} ')
    return text.split()


def parse_formula(text: str):

    tokens = tokenize(text)
    pos = 0

    def parse_expression():
        nonlocal pos
        node = parse_term()

        while pos < len(tokens) and tokens[pos] in ["&", "|", "U"]:
            op_token = tokens[pos]
            pos += 1
            right = parse_term()

            if op_token == "&":
                node = LTLFormula(LTLOperator.AND, node, right)
            elif op_token == "|":
                node = LTLFormula(LTLOperator.OR, node, right)
            elif op_token == "U":
                node = LTLFormula(LTLOperator.UNTIL, node, right)

        return node


    def parse_term():
        nonlocal pos
        token = tokens[pos]

        # NOT
        if token == "!":
            pos += 1
            return LTLFormula(
                operator=LTLOperator.NOT,
                left=parse_term()
            )

        # temporal unary operators
        if token in ["X", "F", "G"]:
            pos += 1
            op_map = {
                "X": LTLOperator.NEXT,
                "F": LTLOperator.EVENTUALLY,
                "G": LTLOperator.ALWAYS
            }

            return LTLFormula(
                operator=op_map[token],
                left=parse_term()
            )

        # parentheses
        if token == "(":
            pos += 1
            node = parse_expression()
            pos += 1  # skip ")"
            return node

        # proposition
        pos += 1
        return LTLFormula(proposition=Proposition(token))


    return parse_expression()
