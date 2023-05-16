from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum


############################################################################################################################
# only the Model has access to the database. η διαχειριση των δεδομενων γινεται ΜΟΝΟ ΑΠΟ ΤΟ ΜΟΝΤΕΛΟ
# σκεψου το μοντελο οτι μπορει να ειναι και αυτονομο, χωρις ui.
############################################################################################################################


@dataclass
class Articulation(str, Enum):
    UP = "up"
    DOWN = "down"


@dataclass
class Duration(str, Enum):
    SIXTEENTH = "16th"
    EIGHTH = "eighth"
    QUARTER = "quarter"
    HALF = "half"
    WHOLE = "whole"


@dataclass
class Fingering(str, Enum):
    P = "p"
    I = "i"
    M = "m"
    A = "a"


@dataclass
class Note:
    noteOnString: Optional[int] = None
    string: Optional[int] = None


@dataclass
class NoteSymbol:
    string: int


@dataclass
class StringFingering:
    string: int
    fingering: Fingering


@dataclass
class StringFingeringWithNote:
    string: int
    fingering: Fingering
    note: int


@dataclass
class Slur:
    start: bool
    end: bool
    string: int


@dataclass
class Triplet(int, Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


@dataclass
class Chord:
    duration: Duration
    accent: Optional[bool] = False
    articulation: Optional[Articulation] = None
    box: Optional[bool] = False # This should be calculated automatically
    header: Optional[Fingering] = field(default_factory=list)# multiple header fingering
    note: Optional[Note] = field(default_factory=list) # list of notes
    noteSymbol: Optional[NoteSymbol] = None
    stringFingering: Optional[StringFingering] = field(default_factory=list)
    stringfingeringWithNote: Optional[StringFingeringWithNote] = field(default_factory=list)
    slur: Optional[Slur] = None
    triplet: Optional[Triplet] = None


@dataclass
class Formula:
    chords: Chord = field(default_factory=list)

    def addChordToFormula(self, Chord):
        self.chords.append(Chord)

    def removeChordFromFormula(self):
        self.chords.pop()

    def multiply(self, multiplier):
        self.chords = self.chords * multiplier

    def reset(self):
        self.chords = []


@dataclass
class FormulaList:
    formulae: List[Formula]


@dataclass
class Page:
    numberOfRows: int
    numberOfColumns: int
    formulaList: List[FormulaList]


@dataclass
class Paragraph:
    pages: List[Page]


@dataclass
class ParagraphSection: # A, B
    # αριθμος παραγραφων to length της λίστας απο κάτω
    paragraphs : List[Paragraph]


@dataclass
class Unit:
    paragraphSection: List[ParagraphSection]


@dataclass
class Chapter:
    units: List[Unit]


@dataclass
class Book:
    chapters: List[Chapter]