import os
import itertools
import copy
import random
from dataclasses import dataclass


@dataclass
class SerialNumber:
    currentIndex = int
    currentNumber = int
    serialNoteNumberList = list[int]

    def __init__(self, serialNoteNumbers, serialNumberType):
        divisor = 8 if serialNumberType == "no repeat" else 12
        divisorList = []
        [
            divisorList.append(idx)
            for idx, element in enumerate(serialNoteNumbers)
            if idx % divisor == 0
        ]
        self.currentIndex = random.choice(divisorList)
        self.serialNoteNumberList = serialNoteNumbers
        self.currentNumber = self.serialNoteNumberList[self.currentIndex]

    def increment(self):
        if self.currentIndex < len(self.serialNoteNumberList) - 1:
            self.currentIndex += 1
            self.currentNumber = self.serialNoteNumberList[self.currentIndex]
        else:
            self.currentIndex = 0
            self.currentNumber = self.serialNoteNumberList[self.currentIndex]


def findTheListOfMuseScoreFiles(bookTitle):
    listOfMSFiles = []
    bookFolder = os.path.join("books", bookTitle)
    for filename in os.listdir(bookFolder):
        if filename.endswith(".mscx"):
            museScoreFile = os.path.join(bookFolder, filename)
            listOfMSFiles.append(museScoreFile)
    return listOfMSFiles


def readSerialNoteNumbers():
    serialNoteNumberList = []
    with open("serial-notes/all-serial-note-numbers.txt", "r") as file:
        for line in file:
            stringNumbers = line.strip().split()
            listElementNumbers = [int(x) for x in stringNumbers]
            serialNoteNumberList.append(listElementNumbers)
    return serialNoteNumberList


def findFinalSerialNumberList(serialNoteNumberList, serialNumberType):
    def noRepeatSerialNumbers(flatList):
        oneDigitList = [
            int(oneDigit) for twoDigits in flatList for oneDigit in str(twoDigits)
        ]
        return oneDigitList

    def duplicateAndRearrangeTripleDigitLists(flatList, a, b, c, d, e, f):
        threeDigitTuple = [
            (int(str(idx)[a:b]), int(str(idx)[c:d]), int(str(idx)[e:f]))
            for idx in flatList
        ]
        oneDigitList = [item for digit in threeDigitTuple for item in digit]
        return oneDigitList

    def duplicateAndRearrangeSixDigitLists(
        flatList, a, b, c, d, e, f, g, h, i, j, k, m
    ):
        sixDigitSubslists = []
        for idx in range(0, len(flatList) - 1, 2):
            sixDigitTuple = [
                int(str(flatList[idx])[a:b]),
                int(str(flatList[idx])[c:d]),
                int(str(flatList[idx])[e:f]),
                int(str(flatList[idx + 1])[g:h]),
                int(str(flatList[idx + 1])[i:j]),
                int(str(flatList[idx + 1])[k:m]),
            ]
            sixDigitSubslists.append(sixDigitTuple)
        oneDigitList = [item for digit in sixDigitSubslists for item in digit]
        return oneDigitList

    flatList = list(itertools.chain(*serialNoteNumberList))
    if serialNumberType == "no repeat":
        serialNoteNumbers = noRepeatSerialNumbers(flatList)
    elif serialNumberType == "first-to-third":
        a, b, c, d, e, f = 0, 1, 1, 2, 0, 1
        serialNoteNumbers = duplicateAndRearrangeTripleDigitLists(
            flatList, a, b, c, d, e, f
        )
    elif serialNumberType == "second-to-third":
        a, b, c, d, e, f = 0, 1, 1, 2, 1, 2
        serialNoteNumbers = duplicateAndRearrangeTripleDigitLists(
            flatList, a, b, c, d, e, f
        )
    elif serialNumberType == "first-to-second":
        a, b, c, d, e, f = 0, 1, 0, 1, 1, 2
        serialNoteNumbers = duplicateAndRearrangeTripleDigitLists(
            flatList, a, b, c, d, e, f
        )
    elif serialNumberType == "second-to-third-first-to-second":
        a, b, c, d, e, f, g, h, i, j, k, m = (0, 1, 1, 2, 1, 2, 0, 1, 0, 1, 1, 2)
        serialNoteNumbers = duplicateAndRearrangeSixDigitLists(
            flatList, a, b, c, d, e, f, g, h, i, j, k, m
        )
    elif serialNumberType == "first-to-second-second-to-third":
        a, b, c, d, e, f, g, h, i, j, k, m = (0, 1, 0, 1, 1, 2, 0, 1, 1, 2, 1, 2)
        serialNoteNumbers = duplicateAndRearrangeSixDigitLists(
            flatList, a, b, c, d, e, f, g, h, i, j, k, m
        )
    return serialNoteNumbers


def saveNewMuseScoreFileWithEmbeddedSerialNoteNumbers(museScoreFile, museScoreFilePath):
    with open(museScoreFilePath, mode="w") as f:
        f.write(museScoreFile)


def findXmlToSubstituteAndEmbedForEachMuseScoreFile(
    museScoreFile, museScoreFilePath, textOccurrencesInFile, serialNumber
):
    def findXmlToSubstitute(museScoreFile, occurrence):
        xmlToSubstitute = ""
        charactherCount = 0
        while (
            ("</pitch>" not in xmlToSubstitute)
            or ("</fret>" not in xmlToSubstitute)
            # or ("</tpc>" not in xmlToSubstitute)
        ):
            xmlToSubstitute += museScoreFile[occurrence + charactherCount]
            charactherCount += 1
        return xmlToSubstitute

    def findNumberToSubstitute(xmlToSubstitute, openingTag, closingTag):
        openingTagIndex = xmlToSubstitute.find(openingTag)
        closingTagIndexWithoutTheClosingTag = xmlToSubstitute.find(closingTag)
        closingTagIndex = closingTagIndexWithoutTheClosingTag + len(
            closingTag
        )  # Number of characters in closing tag
        XMLstring = xmlToSubstitute[openingTagIndex:closingTagIndex]
        XMLwithoutOpeningTag = XMLstring.replace(openingTag, "")
        XMLwithoutOpeningAndClosingTags = XMLwithoutOpeningTag.replace(closingTag, "")
        if " " in XMLwithoutOpeningAndClosingTags:
            XMLNumberAsString = XMLwithoutOpeningAndClosingTags.replace(" ", "")
        else:
            XMLNumberAsString = copy.deepcopy(XMLwithoutOpeningAndClosingTags)
        number = int(XMLNumberAsString)
        return number

    def checkIfThisIsNoteToEmbedOrNot(fretNumber):
        # We substitute/embed only notes with fret number equal to zero
        return fretNumber == 0

    def substitudeTagNumber(xmlToSubstitute, numberToEmbed, openingTag, closingTag):
        openingTagIndex = xmlToSubstitute.find(openingTag)
        closingTagIndex = xmlToSubstitute.find(closingTag) + len(closingTag)
        stringToSubstitute = xmlToSubstitute[openingTagIndex:closingTagIndex]
        if openingTag != "<tpc>" and closingTag != "</tpc>":
            stringToEmbed = openingTag + str(numberToEmbed) + closingTag
        else:
            stringToEmbed = ""
        XMLwithTagReplaced = xmlToSubstitute.replace(stringToSubstitute, stringToEmbed)
        return XMLwithTagReplaced

    def findTextToEmbed(
        xmlToSubstitute,
        fretNumberToSubstitute,
        pitchNumberToSubstitute,
        # tpcNumberToSubstitute,
        serialNumber,
    ):
        fretNumberToEmbed = fretNumberToSubstitute + serialNumber

        xmlToSubstitute = substitudeTagNumber(
            xmlToSubstitute, fretNumberToEmbed, "<fret>", "</fret>"
        )

        pitchNumberToEmbed = pitchNumberToSubstitute + serialNumber

        xmlToSubstitute = substitudeTagNumber(
            xmlToSubstitute, pitchNumberToEmbed, "<pitch>", "</pitch>"
        )

        # tpcNumberToEmbed = copy.deepcopy(tpcNumberToSubstitute)
        tpcNumberToEmbed = ""

        xmlToSubstitute = substitudeTagNumber(
            xmlToSubstitute, tpcNumberToEmbed, "<tpc>", "</tpc>"
        )

        return xmlToSubstitute

    for occurrence in textOccurrencesInFile:
        xmlToSubstitute = findXmlToSubstitute(museScoreFile, occurrence)
        fretNumberToSubstitute = findNumberToSubstitute(
            xmlToSubstitute, "<fret>", "</fret>"
        )
        substituteOrNot = checkIfThisIsNoteToEmbedOrNot(fretNumberToSubstitute)
        if substituteOrNot:
            pitchNumberToSubstitute = findNumberToSubstitute(
                xmlToSubstitute, "<pitch>", "</pitch>"
            )

            # tpcNumberToSubstitute = findNumberToSubstitute(
            #     xmlToSubstitute, "<tpc>", "</tpc>"
            # )
            currentSerialNumber = serialNumber.currentNumber
            textToEmbed = findTextToEmbed(
                xmlToSubstitute,
                fretNumberToSubstitute,
                pitchNumberToSubstitute,
                # tpcNumberToSubstitute,
                currentSerialNumber,
            )

            museScoreFile = (
                museScoreFile[:occurrence]
                + textToEmbed
                + museScoreFile[occurrence + len(xmlToSubstitute) :]
            )

            serialNumber.increment()
    saveNewMuseScoreFileWithEmbeddedSerialNoteNumbers(museScoreFile, museScoreFilePath)


def substituteSerialNoteNumbersOnAllMuseScoreFiles(museScoreFiles, serialNumber):
    for index, museScoreFilePath in enumerate(museScoreFiles):
        print(f"Embedding Serial Notes to file {index+1}/{len(museScoreFiles)}...")
        with open(museScoreFilePath, "r") as file:
            museScoreFile = file.read()
            textReference = "<text>x</text>"
            textOccurrencesInFile = [
                i
                for i in range(len(museScoreFile))
                if museScoreFile.startswith(textReference, i)
            ]
            findXmlToSubstituteAndEmbedForEachMuseScoreFile(
                museScoreFile,
                museScoreFilePath,
                textOccurrencesInFile,
                serialNumber,
            )
    print("Serial Note Substitution Done!")


def main(bookTitle, serialNumberType):
    museScoreFiles = findTheListOfMuseScoreFiles(bookTitle)
    serialNoteNumberList = readSerialNoteNumbers()
    finalSerialNoteNumbers = findFinalSerialNumberList(
        serialNoteNumberList, serialNumberType
    )
    initialSerialNumber = SerialNumber(finalSerialNoteNumbers, serialNumberType)
    substituteSerialNoteNumbersOnAllMuseScoreFiles(museScoreFiles, initialSerialNumber)


# 1. να παιρνει σε λουπα τους serial note αριθμους και να τους αντικαθιστα


# 2. να φτιαξω το μαλακισμενο συμβολο νοτας με το νουμερο μεσα - ελεος
# 3. να φτιαξω το header fingering
# 4. να κανει εξπορτ το pdf του musescore
# 5. να κανει merge όλα τα pdfs


if __name__ == "__main__":
    # 1. Book Title
    bookTitle = "book-IX"

    # 2. Select the type of serial numbers repeat
    # "no repeat"
    # "first-to-third"
    # "second-to-third"
    # "first-to-second"
    # "second-to-third-first-to-second"
    # "first-to-second-second-to-third"

    serialNumberType = "no repeat"

    main(bookTitle, serialNumberType)
