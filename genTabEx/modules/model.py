from dataclasses import dataclass, field
from typing import Optional, List
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
@dataclass
class Variation:
    formulas : Optional[Formula] = field(default_factory=list)


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


@dataclass
class SerialNoteNumber:
    twelveNoteLengthSerialNotes: bool = False
    serialNoteNumberList: list = field(default_factory=list)
    currentNoteNumbers: list = field(default_factory=list)
    currentStep: int = field(default_factory=int)

    def getSerialNoteNumberList(self):
        if self.twelveNoteLengthSerialNotes:
            serialNumberFile = "data/12-note-length-serial-note-numbers.txt"
        else:
            serialNumberFile = "data/serial-note-numbers.txt"
            
        with open(serialNumberFile) as serialNoteNumbersFile:
            serialNoteNumbers = serialNoteNumbersFile.read()
            serialNoteNumbersListWithoutCommas = serialNoteNumbers.split("\n")
            serialNoteNumberList = []
            for row in serialNoteNumbersListWithoutCommas:
                element = [int(x) for x in row.split(" ")]
                serialNoteNumberList.append(element)
        return serialNoteNumberList
    

    def whichSerialNoteNumberFile(self):
        if self.twelveNoteLengthSerialNotes:
            currentStepFile = "data/current-serial-note-number-12-note-length.pkl"
        else:
            currentStepFile = "data/current-serial-note-number.pkl" 
        return currentStepFile


    def getCurrentStep(self):
        with open(self.whichSerialNoteNumberFile(), 'rb') as pklFile:
            currentStep = pickle.load(pklFile)
        return currentStep


    def getCurrentNoteNumbers(self):
        currentNoteNumbersList = self.serialNoteNumberList[self.currentStep]
        return currentNoteNumbersList
    

    def __post_init__(self):
        self.serialNoteNumberList = self.getSerialNoteNumberList()
        self.currentStep = self.getCurrentStep()
        self.currentNoteNumbers = self.getCurrentNoteNumbers()

    
    def goToTheNextStep(self):
        if self.currentStep < len(self.serialNoteNumberList)-1:
            self.currentStep += 1 
        else:
            self.currentStep = 0
        self.currentNoteNumbers = self.getCurrentNoteNumbers()


    def saveCurrentStep(self):
        with open(self.whichSerialNoteNumberFile(), 'wb') as f:
            pickle.dump(self.currentStep, f) 



@dataclass
class CustomSerialNoteNumberList:
    serialNoteNumberList:  List = field(default_factory=lambda: [])

    def appendSerialNoteNumbersToList(self, x):
        self.serialNoteNumberList.append(x)


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


@dataclass
class SerialNumberRepeatingType(int, Enum):
    firstCharacterToThird = 1
    secondCharacterToThird = 2
    firstCharacterDoubling = 3
    firstCharacterToThirdSecondCharacterToThird = 4
    secondCharacterToThirdFirstCharacterToThird = 5



# sto render tha mpoun ta noumera kai h alfavitikh seira ton paragraphon dld I,II,III H IA,IB,IC..
# H STA VARIATIONS A1, B1, C1 ή A1,A2,B1,B2,C1,C2



if __name__ == '__main__':
    print("fml - model")