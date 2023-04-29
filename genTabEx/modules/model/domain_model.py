from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


############################################################################################################################
# only the Model has access to the database. η διαχειριση των δεδομενων γινεται ΜΟΝΟ ΑΠΟ ΤΟ ΜΟΝΤΕΛΟ
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


# VARIATION = TIMES TO REPEAT THE HEADER PATTERNS
# DON'T CHANGE IT. IT MAKES SENSE IF YOU TAKE A LOOK AT THE BOOKS
@dataclass
class Variation:
    formulas : Formula = field(default_factory=list)


@dataclass
class Paragraph:
    variations : Variation = field(default_factory=list)
    

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




chord1 = Chord(duration=Duration.EIGHTH, accent=False, articulation = Articulation.UP, box=False, header=[Fingering.A, Fingering.P],
               note = Note(noteOnString=1, string=3), NoteSymbol=False, 
               stringFingering = StringFingering(fingering=Fingering.I,string=6), stringfingeringWithNote=False,
               slur= Slur(start=True, string=2, end=False), triplet=Triplet.FIRST)


formula1 = Formula()
formula2 = Formula()
formula3 = Formula()
formula4 = Formula()
variation1 = Variation()
variation2 = Variation()
variation3 = Variation()
variation4 = Variation()
paragraph1 = Paragraph()
paragraph2 = Paragraph()
paragraph3 = Paragraph()
paragraph4 = Paragraph()
unit1 = Unit()
unit2 = Unit()
unit3 = Unit()
unit4 = Unit()
chapter1 = Chapter()
chapter2 = Chapter()
book = Book(stringNumber=6, title="First Book", subtitle="test1", chapters= [chapter1, chapter2])