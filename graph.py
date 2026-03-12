from state import State
from arc import Arc

class Graph:
    def __init__(self):
        self.states = {}  # dictionary: state_name -> State object
        self.arcs = []    # list of Arc objects

    def add_state(self, state: State):
        if state.name in self.states:
            raise ValueError(f"State {state.name} already exists")
        self.states[state.name] = state

    def add_arc(self, from_state_name: str, to_state_name: str):
        if from_state_name not in self.states or to_state_name not in self.states:
            raise ValueError("Both states must exist in the graph")
        arc = Arc(self.states[from_state_name], self.states[to_state_name])
        self.arcs.append(arc)

    def neighbors(self, state_name: str):
        """Return a list of states directly reachable from given state"""
        return [arc.to_state for arc in self.arcs if arc.from_state.name == state_name]

    def __str__(self):
        state_names = ', '.join(self.states.keys())
        arcs_str = ', '.join([f"{arc.from_state.name}->{arc.to_state.name}" for arc in self.arcs])
        return f"Graph(States=[{state_names}], Arcs=[{arcs_str}])"
