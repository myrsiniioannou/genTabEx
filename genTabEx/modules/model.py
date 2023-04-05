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
class Slur(int, Enum):
    START = 1
    END = 2


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
    header: Optional[Fingering] = field(default_factory=list)# if there are a lot of header fingerings like ppp then the str could be more than 1 character long
    note: Optional[Note] = None
    noteSymbol: Optional[NoteSymbol] = None
    stringFingering: Optional[StringFingering] = None
    stringfingeringWithNote: Optional[StringFingeringWithNote] = None
    slur: Optional[Slur] = None
    triplet: Optional[Triplet] = None


@dataclass
class Formula:
    number: int
    chordNumber: int
    chords: Chord = field(default_factory=list)


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