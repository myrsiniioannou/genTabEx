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


def flatten(listToFlatten):
    return [item for sublist in listToFlatten for item in sublist]


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

    def duplicateAndRearrangeTripleDigitLists(
        flatList,
        first_number,
        second_number,
        third_number,
        fourth_number,
        fifth_number,
        sixth_number,
    ):
        threeDigitTuple = [
            (
                int(str(idx)[first_number:second_number]),
                int(str(idx)[third_number:fourth_number]),
                int(str(idx)[fifth_number:sixth_number]),
            )
            for idx in flatList
        ]
        oneDigitList = [item for digit in threeDigitTuple for item in digit]
        return oneDigitList

    def duplicateAndRearrangeSixDigitLists(
        flatList,
        first_number,
        second_number,
        third_number,
        fourth_number,
        fifth_number,
        sixth_number,
        seventh_number,
        eighth_number,
        nineth_number,
        tenth_number,
        eleventh_number,
        twelveth_number,
    ):
        sixDigitSubslists = []
        for idx in range(0, len(flatList) - 1, 2):
            sixDigitTuple = [
                int(str(flatList[idx])[first_number:second_number]),
                int(str(flatList[idx])[third_number:fourth_number]),
                int(str(flatList[idx])[fifth_number:sixth_number]),
                int(str(flatList[idx + 1])[seventh_number:eighth_number]),
                int(str(flatList[idx + 1])[nineth_number:tenth_number]),
                int(str(flatList[idx + 1])[eleventh_number:twelveth_number]),
            ]
            sixDigitSubslists.append(sixDigitTuple)
        oneDigitList = [item for digit in sixDigitSubslists for item in digit]
        return oneDigitList

    flatList = list(itertools.chain(*serialNoteNumberList))
    if serialNumberType == "no repeat":
        serialNoteNumbers = noRepeatSerialNumbers(flatList)
    elif serialNumberType == "first-to-third":
        (
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
        ) = (
            0,
            1,
            1,
            2,
            0,
            1,
        )
        serialNoteNumbers = duplicateAndRearrangeTripleDigitLists(
            flatList,
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
        )
    elif serialNumberType == "second-to-third":
        (
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
        ) = (
            0,
            1,
            1,
            2,
            1,
            2,
        )
        serialNoteNumbers = duplicateAndRearrangeTripleDigitLists(
            flatList,
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
        )
    elif serialNumberType == "first-to-second":
        (
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
        ) = (
            0,
            1,
            0,
            1,
            1,
            2,
        )
        serialNoteNumbers = duplicateAndRearrangeTripleDigitLists(
            flatList,
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
        )
    elif serialNumberType == "second-to-third-first-to-second":
        (
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
            seventh_number,
            eighth_number,
            nineth_number,
            tenth_number,
            eleventh_number,
            twelveth_number,
        ) = (0, 1, 1, 2, 1, 2, 0, 1, 0, 1, 1, 2)
        serialNoteNumbers = duplicateAndRearrangeSixDigitLists(
            flatList,
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
            seventh_number,
            eighth_number,
            nineth_number,
            tenth_number,
            eleventh_number,
            twelveth_number,
        )
    elif serialNumberType == "first-to-second-second-to-third":
        (
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
            seventh_number,
            eighth_number,
            nineth_number,
            tenth_number,
            eleventh_number,
            twelveth_number,
        ) = (0, 1, 0, 1, 1, 2, 0, 1, 1, 2, 1, 2)
        serialNoteNumbers = duplicateAndRearrangeSixDigitLists(
            flatList,
            first_number,
            second_number,
            third_number,
            fourth_number,
            fifth_number,
            sixth_number,
            seventh_number,
            eighth_number,
            nineth_number,
            tenth_number,
            eleventh_number,
            twelveth_number,
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
        while ("</pitch>" not in xmlToSubstitute) or ("</fret>" not in xmlToSubstitute):
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
            stringToEmbed = " " * len(stringToSubstitute)
        XMLwithTagReplaced = xmlToSubstitute.replace(stringToSubstitute, stringToEmbed)
        return XMLwithTagReplaced

    def findTextToEmbed(
        xmlToSubstitute,
        fretNumberToSubstitute,
        pitchNumberToSubstitute,
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

            currentSerialNumber = serialNumber.currentNumber
            textToEmbed = findTextToEmbed(
                xmlToSubstitute,
                fretNumberToSubstitute,
                pitchNumberToSubstitute,
                currentSerialNumber,
            )

            museScoreFile = (
                museScoreFile[:occurrence]
                + textToEmbed
                + museScoreFile[occurrence + len(xmlToSubstitute) :]
            )

            serialNumber.increment()
    saveNewMuseScoreFileWithEmbeddedSerialNoteNumbers(museScoreFile, museScoreFilePath)


def findTextOccurencesInMuseScoreFile(museScoreFile):
    textReference = "<text>x</text>"
    textOccurrencesInFile = [
        i
        for i in range(len(museScoreFile))
        if museScoreFile.startswith(textReference, i)
    ]
    return textOccurrencesInFile


def substituteSerialNoteNumbersOnAllMuseScoreFiles(museScoreFiles, serialNumber):
    for index, museScoreFilePath in enumerate(museScoreFiles):
        print(f"Embedding Serial Notes to file {index+1}/{len(museScoreFiles)}...")
        with open(museScoreFilePath, "r") as museScoreRawFile:
            museScoreFile = museScoreRawFile.read()
            textOccurrencesInFile = findTextOccurencesInMuseScoreFile(museScoreFile)
            findXmlToSubstituteAndEmbedForEachMuseScoreFile(
                museScoreFile,
                museScoreFilePath,
                textOccurrencesInFile,
                serialNumber,
            )
    print("Serial Note Substitution Done!")


def generateHeaderFingeringList(headerFingerings, headerFingeringMultiplications):
    def generateUnitsAndChapters(paragraph, multiplications):
        allParagraphs = (flatten(paragraph)) * multiplications["paragraphs"]
        allUnits = flatten(allParagraphs * multiplications["units"])
        allChapters = allUnits * multiplications["chapters"]
        return flatten(allChapters)

    def findAllpageFingerings(measureFingerings):
        pageFingerings = []
        rowfingerings = []
        for idx, element in enumerate(measureFingerings):
            rowfingerings.append(element)
            if (idx + 1) % headerFingeringMultiplications["columns"] == 0:
                pageFingerings.append(rowfingerings)
                rowfingerings = []
        return pageFingerings

    paragraph = []
    for part in headerFingerings:  # Part A & B
        measureFingerings = [
            element * headerFingeringMultiplications["elementAppearanceInRow"]
            for element in part
        ]

        pageFingerings = findAllpageFingerings(measureFingerings)
        completePage = [
            col * headerFingeringMultiplications["rows"] for col in pageFingerings
        ]
        paragraph.append(completePage)

        headerFingeringsInOneCharacterList = generateUnitsAndChapters(
            paragraph, headerFingeringMultiplications
        )

    return headerFingeringsInOneCharacterList


def substitueHeaderFingering(museScoreFiles, headerFingeringListToEmbed):
    for index, museScoreFilePath in enumerate(museScoreFiles):
        print(f"Embedding Header Fingerings {index+1}/{len(museScoreFiles)}...")
        with open(museScoreFilePath, "r") as museScoreRawFile:
            museScoreFile = museScoreRawFile.read()
            fingeringOccurrencesInFile = findTextOccurencesInMuseScoreFile(
                museScoreFile
            )
            print(fingeringOccurrencesInFile)


###########
#          # exei meinei na kano antikatastash se kathe fingeringOccurrencesInFile ena ena ta elements tou headerFingeringListToEmbed


###########################################################################################
#
#
##
#######################################################################################3
#
#


def main(bookTitle, serialNumberType, headerFingerings, headerFingeringMultiplications):
    museScoreFiles = findTheListOfMuseScoreFiles(bookTitle)
    serialNoteNumberList = readSerialNoteNumbers()
    finalSerialNoteNumbers = findFinalSerialNumberList(
        serialNoteNumberList, serialNumberType
    )
    initialSerialNumber = SerialNumber(finalSerialNoteNumbers, serialNumberType)
    substituteSerialNoteNumbersOnAllMuseScoreFiles(museScoreFiles, initialSerialNumber)
    # headerFingeringsInOneCharacterList = generateHeaderFingeringList(
    #     headerFingerings, headerFingeringMultiplications
    # )
    # substitueHeaderFingering(museScoreFiles, headerFingeringsInOneCharacterList)


# 1. exei meinei na kano antikatastash se kathe fingeringOccurrencesInFile ena ena ta elements tou headerFingeringListToEmbed
# 2. να κανει εξπορτ το pdf του musescore
# 3. να κανει merge όλα τα pdfs


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
    headerFingerings = [
        [  # Part A
            ["i", "m", "i"],
            ["m", "i", "m"],
            ["m", "a", "m"],
            ["a", "m", "a"],
            ["i", "a", "i"],
            ["a", "i", "a"],
        ],
        # If the paragraphs follow thE sequence IA->ISECOND_NUMBER, IIA->IIB etc
        # then put all the fingerings in Part A and treat the two paragraphs as one.
        [  # Part B
            ["i", "m", "a"],
            ["i", "a", "m"],
            ["m", "i", "a"],
            ["m", "a", "i"],
            ["a", "m", "i"],
            ["a", "i", "m"],
        ],
    ]
    headerFingeringMultiplications = {
        "elementAppearanceInRow": 4,
        "columns": 1,
        "rows": 7,
        "paragraphs": 7,
        "units": 4,
        "chapters": 1,
    }

    main(bookTitle, serialNumberType, headerFingerings, headerFingeringMultiplications)
