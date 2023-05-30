from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum


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
    index: int
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
    formulaList: List[FormulaList]

@dataclass
class Paragraph:
    pages: List[Page]

@dataclass
class Section: # A, B
    paragraphs : List[Paragraph]
    variationRepeats: int

@dataclass
class Unit:
    sections: List[Section]

@dataclass
class Chapter:
    units: List[Unit]

@dataclass
class Book:
    chapters: List[Chapter]