import sys
sys.path.append('modules/model')
sys.path.append('modules/view')
import os
from format import *
from domain_model import *
from evolutions import *
from render import *
from serial_note_numbers import *
from data_generation import *
import json




serialNoteNumber = SerialNoteNumber(serialNumberRepeatingType=SerialNumberRepeatingType.firstCharacterDoubling,
                                    twelveNoteLengthSerialNotes= True)

customSerialNoteNumberList = CustomSerialNoteNumberList(serialNoteNumberList = None)


chord1 = Chord(duration=Duration.EIGHTH, accent=False, articulation = Articulation.UP, box=False, header=None,
               note = Note(noteOnString=0, string=3), noteSymbol= NoteSymbol(string=3), stringFingering = StringFingering(fingering=Fingering.I,string=6), stringfingeringWithNote=False,
               slur= Slur(start=True, string=2, end=False), triplet=Triplet.FIRST)
chord2 = Chord(duration=Duration.HALF, accent=True, articulation = Articulation.DOWN, box=True, header=None,
               note = Note(noteOnString=0, string=4), stringFingering = StringFingeringWithNote(string=4, fingering=Fingering.A, note=5),
               triplet=Triplet.SECOND)
chord3 = Chord(duration=Duration.SIXTEENTH, accent=False, articulation = Articulation.DOWN, box=False, header=None,
               note = Note(noteOnString=0, string=3), noteSymbol= NoteSymbol(string=6),
               stringFingering = StringFingering(fingering=Fingering.A,string=4), stringfingeringWithNote=False,
               slur= Slur(start=False, string=5, end=True), triplet=Triplet.THIRD)
chord4 = Chord(duration=Duration.WHOLE, accent=True, box=False, header=None,
               note = Note(noteOnString=0, string=6), stringFingering = StringFingering(fingering=Fingering.I,string=6), stringfingeringWithNote=False,
               slur= Slur(start=True, string=2, end=False), triplet=Triplet.FIRST)



formula1 = Formula(chords=[chord1, chord1, chord1, chord1], index=1)
formula2= Formula(chords=[chord2, chord2, chord2, chord2], index=2)
formula3= Formula(chords=[chord3, chord3, chord3, chord3], index=3)
formula4= Formula(chords=[chord4, chord4, chord4, chord4], index=4)
formula5= Formula(chords=[chord4, chord4, chord4, chord4], index=5)
formula6= Formula(chords=[chord4, chord4, chord4, chord4], index=6)
formula7= Formula(chords=[chord4, chord4, chord4, chord4], index=7)
formula8= Formula(chords=[chord4, chord4, chord4, chord4], index=8)
formula1.multiply(3)
formula2.multiply(3)
formula3.multiply(3)
formula4.multiply(3)
formula5.multiply(3)
formula6.multiply(3)
formula7.multiply(3)
formula8.multiply(3)
formulaList1 = FormulaList(formulae=[formula1, formula2, formula3, formula4, formula5, formula6, formula7, formula8])
#formulaList1 = FormulaList(formulae=[formula1, formula2, formula3, formula4])
evolution1 = Evolution(type=EvolutionType.stringAscending, fingeringNotNote= True, chordNumber =[1,5],
                       string=2, stringStep=1)



format1 = Format(
                stringNumber=6,
                title="test",
                subtitle=" 1",
                numberOfRows=6,
                numberOfColumns=2,
                paragraphOrderType=ParagraphOrderType.paragraphNumberFirst,
                headerRepeatFormat=HeaderRepeatFormat(rows=1,columns=2),
                horizontalFormat=False,
                variationRepeats = [],
                formulaRepeats=[6,6,6,6,6,6,6,6],
                beams={6:BeamType.doubleLine, 10:BeamType.singleLine}
                )






################################ DATA GENERATION ################################


def generatepartition(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i : i+size]


def flattenList(lst):
    return [item for sublist in lst for item in sublist]


def verticalFormatList(formulaelst, format):
    print(format.numberOfFormulasPerPage)


def errorMessage():
    print("Error with the lengtht of formula repeats. Check and try again.")


def transposeTheListOfFormulas(pageListOfFormulae, format):
    transposedPageListOfFormulae = []
    try:
        for page in pageListOfFormulae:
            columnList = []
            for element in range(format.numberOfRows):
                for formula in page:
                    columnList.append(formula[element])
            transposedPageListOfFormulae.append(columnList)
    except:
        errorMessage()
    return transposedPageListOfFormulae


def divideTheFormulaArraysIntoTheNumberOfRows(formulaList, format):
    horizontalFormulaList = []
    for formula in formulaList:
        if len(formula) != format.numberOfRows:
            dividedList = list(generatepartition(formula, format.numberOfRows))
            horizontalFormulaList.extend(dividedList)
        else:
            horizontalFormulaList.append(formula)
    return horizontalFormulaList


def verticalFormatTransformation(formulaList, format):
    horizontalFormulaList = divideTheFormulaArraysIntoTheNumberOfRows(formulaList, format)
    pageListOfFormulae = list(generatepartition(horizontalFormulaList, format.numberOfColumns))
    transposedPageListOfFormulae = transposeTheListOfFormulas(pageListOfFormulae, format)
    return transposedPageListOfFormulae


def generateParagraph(formulae, format):
    formulaList = [[formula]*format.formulaRepeats[index] for index, formula in enumerate(formulae)]
    flat_list = flattenList(formulaList)
    pageListOfFormulae = list(generatepartition(flat_list, format.numberOfFormulasPerPage))
    finalList = verticalFormatTransformation(formulaList, format) if not format.horizontalFormat else pageListOfFormulae.copy()
    return finalList


def checkFormatInputForErrors(format):
    error = True
    for repeats in format.formulaRepeats:
        if ((format.horizontalFormat and not repeats % format.numberOfColumns == 0)
            or
            (not format.horizontalFormat and not repeats % format.numberOfRows == 0)):
            errorMessage()
            error = False
            break
    return error



def generatePart(formulaList, partType, format):
    part = None
    if checkFormatInputForErrors(format):
        # if  partType == "Book":
        #     part = generateBook(formulaList.formulae, format)
        # elif  partType == "Chapter":
        #     part = generateChapter(formulaList.formulae, format)
        # elif  partType == "Unit":
        #     part = generateUnit(formulaList.formulae, format)
        # elif  partType == "Section": 
        #     part = generateSection(formulaList.formulae, format)
        if  partType  == "Paragraph":
            part = generateParagraph(formulaList.formulae, format)
    return part




# 1. section generations
# 2. single / multiformula. wtf is this 
# 3. apply evolutions
#    4. Export JSON
# 5. book variations
# 6. extensions - continue process
# 7. render
#     8. Make the stupid new symbol
#     9. auto build the sizes
# 10. Auto first page with each unit etc. check the example
# 11. finalize the Book
#     12. combine chapters
#     13. introduction (check the word document)
#     14. One bar in unit page
#     15. Pagination
#     16. covers
#     17. Pdf
# 18. Make the UI
# 19. Setup file on git
#     20.Add musescore
#     21.test installation
#     22.Auto create folders
#     23. Picke file position ->0
#     24. VSCODE paths. Change all the paths
#     25. Test on empty new environment





partType2 = "Chapter"
partType3 = "Unit"
partType4 = "Section"
partType5 = "Paragraph"
generation = generatePart(formulaList1, partType4, format1)
print(generation)




outputDirectory = r"C:\Users\merse\Desktop\genTabEx\genTabEx\modules\model\JSONTEST.json"
with open(outputDirectory, 'w', encoding='utf-8') as f:
    json.dump(generation, f, indent=3, default=vars, ensure_ascii=False)







# import pickle
# with open("data/current-serial-note-number-12-note-length.pkl", 'wb') as f:  # open a text file
#     pickle.dump(28, f) # serialize the list


# with open("data/current-serial-note-number-12-note-length.pkl", 'rb') as f:
#     b = pickle.load(f)

# print(b)









if __name__ == '__main__':
    pass

