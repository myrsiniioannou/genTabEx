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
class ChapterGeneration():
    numberOfUnits: List[int]

@dataclass
class BookGeneration():
    numberOfChapters: int


@dataclass
class Format():
    stringNumber: int
    title: str
    subtitle: str
    numberOfRows: int
    numberOfColumns: int
    paragraphOrderType: ParagraphOrderType
    headerRepeatFormat: HeaderRepeatFormat
    beams: Dict[int, BeamType] # int is the chord number of the formula
    variationRepeats: int #  (USUALLY IT'S PAGES) variations are as many as the number of paragraphs for each section
    horizontalFormat: bool
    formulaRepeats: List[int] # EACH ELEMENT REPEATS
    numberOfFormulasPerPage: list = field(default_factory=list)
    
    def getNumberOfFormulasPerPage(self):
        return self.numberOfColumns * self.numberOfRows

    def __post_init__(self):
        self.numberOfFormulasPerPage = self.getNumberOfFormulasPerPage()



# @dataclass
# class Format():
#     stringNumber: int
#     title: str
#     subtitle: str
#     numberOfRows: int
#     numberOfColumns: int
#     paragraphOrderType: ParagraphOrderType
#     headerRepeatFormat: HeaderRepeatFormat
#     numberOfParagraphs : List[int] # each element is the number of paragraphs for each section
#     numberOfSections: List[int] # each element is the number of sections for each unit
#     variationRepeats: List[int] #  (USUALLY IT'S PAGES) variations are as much as the number of paragraphs for each section
#     numberOfUnits: List[int] # each element is the number of sections for each chapter
#     numberOfChapters: int # each element is the number of sections for each book
#     horizontalFormat: bool
#     formulaRepeatTimes: List[int] # how many times to repeat each formula in the formula list
#     beams: Dict[int, BeamType] # int is the chord number of the formula
#     numberOfFormulasPerPage: list = field(default_factory=list)
    
#     def getNumberOfFormulasPerPage(self):
#         return self.numberOfColumns * self.numberOfRows

#     def __post_init__(self):
#         self.numberOfFormulasPerPage = self.getNumberOfFormulasPerPage()