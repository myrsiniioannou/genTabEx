from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


@dataclass
class RenderType(int, Enum):
    newBook = 1
    bookExtension = 2
    bookVariation = 3


@dataclass
class BookInfo():
    title: str
    subtitle: str
    numberOfStrings: int


@dataclass
class NotationInfo():
    numberOfFormulasPerPage: int
    numberOfRowsPerPage: int
    numberOfColumnsPerPage: int
    numberOfChordsPerFormula: int

    
@dataclass
class ParagraphOrder(int, Enum):
    alphabetical = 1 # IA, IB, IC   ta A,B,C EINAI SUBPARAGRAPHS
    doubleAlphabetical = 2 # IA, IIA, IIIA, IVA... IB, IIB, IIIB IVB...


@dataclass
class BeamType(int, Enum):
    noLine = 1
    singleLine = 2
    doubleLine = 3


@dataclass
class HeadingType(int, Enum):
    single = 1 #### VARIATION 1 ####
    double = 2 #### F1A ## F2A ####
    none: 3    


@dataclass
class HeaderRepeatFormat():
     columns: int
     rows: int


@dataclass
class Format():
    paragraphType: ParagraphOrder
    heading: HeadingType
    headerRepeatFormat: HeaderRepeatFormat
    numberOfParagraphsPerUnit: int
    numberOfSubparagraphsPerUnit: int
    numberOfVariationPages: int
    formulaRepeatHorizontalFormat: bool # horizontal true, vertical false.   
    formulaLetterVisibility: bool
    variationTitleVisibility: bool
    numberOfFormulaMeasures: int
    beams: BeamType = field(default_factory=list)
    headingParagraphLetterVisibility: bool = field(default_factory=bool)


    def getHeadingParagraphLetterVisibility(self):
        self.headingParagraphLetter = True if not self.formulaRepeatHorizontalFormat else False


    def __post_init__(self):
        self.headingParagraphLetter = self.headingParagraphLetterVisibility()


