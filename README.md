# LTL Model Checker (Python)

A simple **Linear Temporal Logic (LTL) model checker** written in Python.
This project allows you to define a **state transition system (graph)** and verify **LTL formulas** interactively from the terminal.

The program loads a graph from a JSON file, then lets the user type formulas that are checked against the model until the user quits.

---

# Project Structure

```
.
├── main.py          # Application entry point (interactive CLI)
├── utils.py         # Graph loader and LTL formula parser
├── verifier.py      # LTL verification logic

├── graph.py         # Graph structure (states + arcs)
├── arc.py           # Transition between states
├── state.py         # State representation
├── proposition.py   # Atomic propositions

├── LTL.py           # LTL operators enum and formula class

├── graph.json       # Example graph input file
```

---

# Requirements

* Python **3.9+**
* No external libraries required

Run with the standard Python interpreter.

---

# How the System Works

The model checker verifies **LTL properties** on a **transition system**.

A transition system consists of:

* **States** (`s0`, `s1`, ...)
* **Propositions** (atomic properties like `p`, `q`)
* **Arcs** (transitions between states)

Each state can contain **zero or more propositions** that are true in that state.

Example:

```
s0: {p}
s1: {}
s2: {q}
```

---

# Graph Input File

The graph must be defined in a **JSON file**.

Example `graph.json`:

```json
{
  "states": [
    {"name": "s0", "props": ["p"]},
    {"name": "s1", "props": []},
    {"name": "s2", "props": ["q"]}
  ],
  "arcs": [
    ["s0","s1"],
    ["s1","s2"],
    ["s2","s1"]
  ]
}
```

Explanation:

### States

Each state contains:

```
name  -> state identifier
props -> list of propositions true in this state
```

Example:

```
s0 has proposition p
s2 has proposition q
```

### Arcs

Arcs define **transitions between states**.

```
["s0","s1"]
```

means:

```
s0 → s1
```

---

# Supported LTL Operators

| Operator | Meaning    | Example |    |    |
| -------- | ---------- | ------- | -- | -- |
| `!`      | NOT        | `!p`    |    |    |
| `&`      | AND        | `p & q` |    |    |
| `        | `          | OR      | `p | q` |
| `X`      | Next       | `X p`   |    |    |
| `F`      | Eventually | `F q`   |    |    |
| `G`      | Always     | `G p`   |    |    |
| `U`      | Until      | `p U q` |    |    |

Parentheses are supported for grouping.

---

# Example Formulas

Atomic proposition:

```
p
```

Eventually:

```
F q
```

Always:

```
G p
```

Next state:

```
X p
```

Until:

```
p U q
```

Complex formulas:

```
F (p & X q)

G (p | F q)

!(p & q)

G (p U q)
```

---

# Running the Program

From the project folder:

```
python main.py
```

The program loads `graph.json` automatically.

You will see an interactive prompt.

Example:

```
LTL Model Checker
Examples: F q , G p , p U q
Type q to quit
```

---

# Example Session

```
LTL> F q
Result: True

LTL> G p
Result: False

LTL> F (p & X q)
Result: True

LTL> q
Bye!
```

Typing `q` exits the program.

---

# Example Graph Behavior

Given the graph:

```
s0 -> s1 -> s2
       ^    |
       |____|
```

with:

```
s0: {p}
s1: {}
s2: {q}
```

Then:

```
F q = True
```

because `q` eventually becomes true in state `s2`.

But:

```
G p = False
```

because `p` is not true in all reachable states.

---

# Future Improvements

Possible extensions:

* Counterexample generation when a formula fails
* Graph visualization
* Full LTL grammar parser
* Support for implication (`->`)
* Multiple initial states
* Petri net to transition system conversion

---

# Educational Purpose

This project is intended as a **learning implementation of LTL model checking** for courses on:

* Formal Verification
* Model Checking
* Temporal Logic
* Concurrent Systems
