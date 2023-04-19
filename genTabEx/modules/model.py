from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
import pickle


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

    def removeChordFromFormula(self):
        self.chords.pop()

    def multiply(self, multiplier):
        self.chords = self.chords * multiplier


@dataclass
class MultiFormula:
    formulas: Formula = field(default_factory=list)


@dataclass
class Variation:
    singleFormulas : Optional[Formula] = field(default_factory=list)
    multiFormulas : Optional[MultiFormula] = field(default_factory=list)


@dataclass
class Paragraph:
    alphabeticalNumber: str
    variations : Optional[Variation] = field(default_factory=list)


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


@dataclass
class EvolutionRange(int, Enum):
    book = 1
    chapter = 2
    unit = 3
    paragraph = 4
    row = 5
    column = 6
    partMeasure = 7


@dataclass
class EvolutionType(int, Enum):
    ascending = 1
    descending = 2
    multiplying = 3


@dataclass
class Evolution:
    type: EvolutionType
    range: EvolutionRange
    step: Optional[int] = 1
    chordNumber: int = field(default_factory=list)
    string: int = field(default_factory=list)
    

@dataclass
class ArrowEvolution:
    chordNumber: int = field(default_factory=list)


@dataclass
class TotalArrowEvolutions:
    ArrowEvolutions: ArrowEvolution = field(default_factory=list)
    

@dataclass
class TotalEvolutions:
    evolutions: Evolution = field(default_factory=list)
    arrowEvolutions: TotalArrowEvolutions = field(default_factory=list)

@dataclass
class SerialNoteNumber:
    serialNoteNumberList: list = field(default_factory=list)
    currentStep: int = field(default_factory=int)
    currentNoteNumbers: list = field(default_factory=list)


    def getSerialNoteNumberList(self):
        with open("data/serial-note-numbers.txt") as serialNoteNumbersFile:
            serialNoteNumbers = serialNoteNumbersFile.read()
            serialNoteNumbersListWithoutCommas = serialNoteNumbers.split("\n")
            serialNoteNumberList = []
            for row in serialNoteNumbersListWithoutCommas:
                element = [int(x) for x in row.split(" ")]
                serialNoteNumberList.append(element)
        return serialNoteNumberList
    

    def getCurrentStep(self):
        with open("data/current-serial-note-number.pkl", 'rb') as pklFile:
            currentStep = pickle.load(pklFile)
        return currentStep


    def getCurrentNoteNumbers(self):
        currentNoteNumbersList = self.serialNoteNumberList[self.currentStep]
        return currentNoteNumbersList
    

    def goToTheNextStep(self):
        self.currentStep += 1 if self.currentStep < len(self.serialNoteNumberList) else 0
        self.currentNoteNumbers = self.getCurrentNoteNumbers()


    def __post_init__(self):
        self.serialNoteNumberList = self.getSerialNoteNumberList()
        self.currentStep = self.getCurrentStep()
        self.currentNoteNumbers = self.getCurrentNoteNumbers()


    # 

    # DEF save it
    

test1 = SerialNoteNumber()
print(test1.serialNoteNumberList)
print("-----------------------------------")
print(test1.currentStep, test1.currentNoteNumbers)
print("-----------------------------------")
test1.goToTheNextStep()
print(test1.currentStep, test1.currentNoteNumbers)
print("-----------------------------------")
test1.goToTheNextStep()
print(test1.currentStep, test1.currentNoteNumbers)

if __name__ == '__main__':
    print("fml - model")