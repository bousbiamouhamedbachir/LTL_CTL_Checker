from enum import Enum
from typing import Optional
from proposition import Proposition

class LTLOperator(Enum):
    NOT = "!"
    AND = "&"
    OR = "|"
    NEXT = "X"
    EVENTUALLY = "F"
    ALWAYS = "G"
    UNTIL = "U"


class LTLFormula:
    def __init__(
        self,
        operator: Optional[LTLOperator] = None,
        left=None,
        right=None,
        proposition: Optional[Proposition] = None
    ):
        self.operator = operator
        self.left = left
        self.right = right
        self.proposition = proposition
