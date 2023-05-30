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
                formulaRepeats=[2,2,2,2,2,2,6,6],
                beams={6:BeamType.doubleLine, 10:BeamType.singleLine}
                )






#############################################3 DATA GENERATION




def generatepartition(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i : i+size]


def flattenList(lst):
    return [item for sublist in lst for item in sublist]


def transposeList(lst, format):
    print(lst)
    for page in lst:
        columnFormulaLists = [[] for i in range(format.numberOfRows)]
        print(page)
        print(columnFormulaLists)
    # flat_list = flattenList(lst)
    # #print(flat_list)
    # pagesList = list(generatepartition(flat_list, format.numberOfFormulasPerPage))
    # print(pagesList)
    # transposedList = []
    # for page in pagesList:
    #     print(page)
    #     columnFomrulaLists = [[] for i in range(format.numberOfRows)]
    #     print(columnFomrulaLists)
    #     #for index, formula in enumerate(page):


    #     print("---------")
        #transposedList.append(columnFomrulaLists)
    
    #print("transposedList:", flattenList(transposedList))
           


    # partitionList2ndLayer = [list(generatepartition(page, format.numberOfColumns)) for page in pagesList] 
    #print(partitionList2ndLayer)
        # try:
        #     T_list = [[[j[i] for j in z] for i in range(format.numberOfRows)] for z in pagesList] 
        #     transposedList = list(generatepartition(flattenList(flattenList(T_list)), format.numberOfFormulasPerPage))
        # except Exception:
        #     print("Wrong number of formula repeats according to number of rows and columns")
        #     transposedList = None
        # print(transposedList)
    
    return None



def generateParagraph(formulae, format):
    #fomrulaList = [[formula]*format.formulaRepeats[index] for index, formula in enumerate(formulae)]
    formulaList = [[formula.index]*format.formulaRepeats[index] for index, formula in enumerate(formulae)]
    flat_list = flattenList(formulaList)
    pageListOfFormulae = list(generatepartition(flat_list, format.numberOfFormulasPerPage))
    if not format.horizontalFormat:
        pageListOfFormulae = transposeList(pageListOfFormulae, format)
    return pageListOfFormulae






def generatePart(formulaList, partType, format):
    # if  partType == "Book":
    #     partType = generateBook(formulaList.formulae, format)
    # elif  partType == "Chapter":
    #     partType = generateChapter(formulaList.formulae, format)
    # elif  partType == "Unit":
    #     partType = generateUnit(formulaList.formulae, format)
    # elif  partType == "Section": 
    #     partType = generateSection(formulaList.formulae, format)
    if  partType  == "Paragraph":
        partType = generateParagraph(formulaList.formulae, format)
    return partType





partType1 = "Book"
partType2 = "Chapter"
partType3 = "Unit"
partType4 = "Section"
partType5 = "Paragraph"
generation = generatePart(formulaList1, partType5, format1)
print(generation)




outputDirectory = r"C:\Users\merse\Desktop\genTabEx\genTabEx\modules\model\JSONTEST.json"
with open(outputDirectory, 'w', encoding='utf-8') as f:
    json.dump(generation, f, indent=3, default=vars, ensure_ascii=False)



if __name__ == '__main__':
    pass







# import pickle
# with open("data/current-serial-note-number-12-note-length.pkl", 'wb') as f:  # open a text file
#     pickle.dump(28, f) # serialize the list


# with open("data/current-serial-note-number-12-note-length.pkl", 'rb') as f:
#     b = pickle.load(f)

# print(b)









if __name__ == '__main__':
    pass

