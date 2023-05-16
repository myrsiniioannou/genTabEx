from dataclasses import dataclass, field
from typing import Dict, List
from enum import Enum
from domain_model import *


@dataclass
class ParagraphOrderType(int, Enum):
    paragraphSectionFirst = 1 # IA, IB, IC
    paragraphNumberFirst = 2 # IA, IIA, IIIA, IVA... IB, IIB, IIIB IVB...


@dataclass
class BeamType(int, Enum):
    defaut = 1
    singleLine = 2
    doubleLine = 3


@dataclass
class HeaderRepeatFormat():
    rows: int
    columns: int
    # gia paradeigma an epanalamvanetai to header sthn proth grammh rows=1,columns=2


@dataclass
class FormulaFormat():
    horizontalFormat: bool
    formulaLetterVisibility: bool


@dataclass
class Format():
    stringNumber: int
    title: str
    subtitle: str
    numberOfRows: int
    numberOfColumns: int
    paragraphOrderType: ParagraphOrderType
    headerRepeatFormat: HeaderRepeatFormat
    formulaFormat: FormulaFormat
    beams: Dict[int, BeamType] # int is the chord number of the formula
    numberOfFormulaRepeats: List[int] # each element is the number that each formula should repeat
    numberOfFormulasPerPage: list = field(default_factory=list)
    
    def getNumberOfFormulasPerPage(self):
        return self.numberOfColumns * self.numberOfRows

    def __post_init__(self):
        self.numberOfFormulasPerPage = self.getNumberOfFormulasPerPage()