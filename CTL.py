from enum import Enum

from enum import Enum

class CTLOperator(Enum):
    EX = "EX"
    AX = "AX"
    EF = "EF"
    AF = "AF"
    EG = "EG"
    AG = "AG"
    EU = "EU"
    AU = "AU"
    AND = "&"
    OR = "|"
    NOT = "!"
class CTLFormula:
    def __init__(self, operator=None, left=None, right=None, proposition=None):
        self.operator = operator
        self.left = left
        self.right = right
        self.proposition = proposition
