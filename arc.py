from state import State

class Arc:
    def __init__(self, state1: State, state2: State):
        self.from_state = state1
        self.to_state = state2

    def __str__(self):
        return f"Arc(from={self.from_state.name}, to={self.to_state.name})"
