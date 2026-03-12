class Proposition:
    def __init__(self, name: str, state: bool = False):
        self.name = name
        self.state = state

    def __str__(self):
        return f"Proposition(name='{self.name}', state={self.state})"
