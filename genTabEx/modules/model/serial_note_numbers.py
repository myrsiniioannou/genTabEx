from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum
import pickle


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
class SerialNumberRepeatingType(int, Enum):
    firstCharacterToThird = 1
    secondCharacterToThird = 2
    firstCharacterDoubling = 3
    firstCharacterToThirdSecondCharacterToThird = 4
    secondCharacterToThirdFirstCharacterToThird = 5