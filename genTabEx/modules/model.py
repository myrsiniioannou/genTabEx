from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

## Domain Model Definition

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
    box: Optional[bool] = False
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


@dataclass
class Paragraph:
    alphabeticalNumber: str
    formulas : Formula = field(default_factory=list)


@dataclass
class Unit:
    number: int
    paragraphs : Paragraph = field(default_factory=list)


@dataclass
class Chapter:
    number: int
    units : Unit = field(default_factory=list)


@dataclass
class Book:
    stringNumber: int
    title: str
    subtitle: str
    chapters : Chapter = field(default_factory=list)




if __name__ == '__main__':
    print("Generative Tablature Exercises")