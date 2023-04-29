from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


@dataclass
class BookPart(int, Enum):
    book = 1
    chapter = 2
    unit = 3
    paragraph = 4
    subParagraph = 5
    variation = 6
    # row = 
    # column = 
    formula = 7
    halfFormula = 8
    oneThirdFormula = 9
    oneFourthFormula = 10


@dataclass
class EvolutionType(int, Enum):
    ascending = 1
    descending = 2
    multiplying = 3


@dataclass
class Evolution:
    type: EvolutionType
    range: BookPart
    stringStep: Optional[int] = 1
    chordNumber: int = field(default_factory=list)
    string: int = field(default_factory=list)
    

@dataclass
class CustomEvolution:
    pass


@dataclass
class ArrowEvolution:
    chordNumber: int = field(default_factory=list)


@dataclass
class TotalArrowEvolutions:
    ArrowEvolutions: ArrowEvolution = field(default_factory=list)
    

@dataclass
class TotalEvolutions:
    evolutions: Evolution = field(default_factory=list)
    customEvolutions: CustomEvolution = field(default_factory=list)
    arrowEvolutions: TotalArrowEvolutions = field(default_factory=list)