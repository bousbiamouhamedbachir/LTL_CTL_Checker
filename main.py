from utils import load_graph, parse_formula, parse_ctl
from verifier import Switcher

def main():
    while True:
        graph_path = input("Enter graph file path (e.g., graph.json): ").strip()
        try:
            graph = load_graph(graph_path)
            break
        except FileNotFoundError:
            print(f"Error: File '{graph_path}' not found. Please try again.")
        except Exception as e:
            print(f"Error loading graph: {e}. Please try again.")

    switcher = Switcher(graph)

    print("Choose logic:")
    print("1 - LTL")
    print("2 - CTL")

    choice = input("> ").strip()

    if choice == "1":
        switcher.set_logic("LTL")
        parse_func = parse_formula
    else:
        switcher.set_logic("CTL")
        parse_func = parse_ctl

    start_state = list(graph.states.keys())[0]

    print(f"Using {switcher.logic}")
    print("Type formulas (examples: F q, G p, p U q for LTL / EX p, AX q, EF r for CTL)")
    print("Type q to quit\n")

    while True:
        user_input = input("Formula> ").strip()
        if user_input.lower() == "q":
            print("Exiting...")
            break

        try:
            formula = parse_func(user_input)
            result = switcher.evaluate(formula, start_state)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
