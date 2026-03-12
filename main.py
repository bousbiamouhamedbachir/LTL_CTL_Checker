from utils import load_graph, parse_formula
from verifier import LTLVerifier


def main():

    graph = load_graph("graph.json")

    verifier = LTLVerifier(graph)

    start_state = list(graph.states.keys())[0]

    print("LTL Model Checker")
    print("Examples: F q , G p , p U q")
    print("Type q to quit\n")

    while True:

        user_input = input("LTL> ").strip()

        if user_input == "q":
            print("Bye!")
            break

        try:
            formula = parse_formula(user_input)

            result = verifier.evaluate(formula, start_state)

            print("Result:", result)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
