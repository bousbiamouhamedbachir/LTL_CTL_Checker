# LTL & CTL Model Checker (Python)

A simple **Linear Temporal Logic (LTL)** and **Computation Tree Logic (CTL)** model checker written in Python.
This project allows you to define a **state transition system (graph)** and verify temporal logic formulas interactively from the terminal.

The program provides an interactive CLI to load a model and choose between LTL and CTL verification.

---

# Project Structure

```
.
├── main.py          # Application entry point (Logic selector & CLI)
├── verifier.py      # Verification logic (LTLVerifier, CTLVerifier, Switcher)
├── utils.py         # Graph loader and Formula parsers (LTL & CTL)
├── LTL.py           # LTL operators and formula representation
├── CTL.py           # CTL operators and formula representation
├── graph.py         # Graph structure (states + arcs)
├── arc.py           # Transition representation
├── state.py         # State representation with propositions
├── proposition.py   # Atomic proposition representation
├── examples/        # Folder containing pre-defined models and exercises
│   ├── ex4.json
│   ├── ex5.json
│   └── ...
└── graph.json       # Default example graph input file
```

---

# Requirements

* Python **3.9+**
* No external libraries required.

---

# How the System Works

The model checker verifies temporal properties on a **Kripke-like transition system**.

A transition system consists of:
* **States**: Labeled identifiers (e.g., `s0`, `s1`).
* **Propositions**: Atomic properties true in specific states (e.g., `p`, `q`).
* **Arcs**: Directed transitions between states.

### Graph Input File Format

The model is defined in a JSON file. You can also include an optional `expressions` field for reference.

```json
{
  "states": [
    {"name": "s0", "props": ["p"]},
    {"name": "s1", "props": []},
    {"name": "s2", "props": ["q"]}
  ],
  "arcs": [
    ["s0", "s1"],
    ["s1", "s2"],
    ["s2", "s1"]
  ],
  "expressions": [
    "F q",
    "G p"
  ]
}
```

---

# Supported Logics

## Linear Temporal Logic (LTL)

Verified over all possible infinite paths from the starting state.

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| `!` | **NOT** | `!p` |
| `&` | **AND** | `p & q` |
| `\|` | **OR** | `p \| q` |
| `X` | **Next** | `X p` |
| `F` | **Eventually** | `F q` |
| `G` | **Always** | `G p` |
| `U` | **Until** | `p U q` |

## Computation Tree Logic (CTL)

Verified over the branching structure of the transition system.

| Operator | Meaning | Example |
| :--- | :--- | :--- |
| `!` | **NOT** | `!p` |
| `&` | **AND** | `p & q` |
| `\|` | **OR** | `p \| q` |
| `EX` | **Exists Next** | `EX p` |
| `AX` | **All Next** | `AX p` |
| `EF` | **Exists Eventually** | `EF p` |
| `AF` | **All Eventually** | `AF p` |
| `EG` | **Exists Globally** | `EG p` |
| `AG` | **All Globally** | `AG p` |
| `EU` | **Exists Until** | `p EU q` |
| `AU` | **All Until** | `p AU q` |

---

# Running the Program

1. Run the main script:
   ```bash
   python main.py
   ```
2. Enter the path to your graph file when prompted (e.g., `graph.json` or `examples/ex4.json`).
3. Choose the logic you wish to use (1 for LTL, 2 for CTL).
4. Enter formulas at the prompt. Type `q` to exit.

---

# Example Session

```text
Enter graph file path (e.g., graph.json): graph.json
Choose logic:
1 - LTL
2 - CTL
> 1
Using LTL
Type formulas (examples: F q, G p, p U q)
Type q to quit

Formula> F q
Result: True

Formula> q
Exiting...
```

---

# Educational Purpose

This project is an educational implementation of model checking algorithms, suitable for courses on Formal Verification, Temporal Logic, and Concurrent Systems.
