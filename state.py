from proposition import Proposition
from typing import List

class State:
    def __init__(self, name: str, propositions: List[Proposition] = None):
        self.name = name
        self.propositions = propositions or []

    def __str__(self):
        props = ', '.join([p.name for p in self.propositions])
        return f"State(name='{self.name}', propositions=[{props}])"
