import sys
sys.path.append('modules/controller')
from controller import *
from domain_model import *
from evolutions import *
from format import *
from serial_note_numbers import *
from dataclasses import dataclass


@dataclass
class Paragraph:
    variationsNumber: int
    numberOfVariationPages: float #0.5 for half-page variation
    # τα variations ousiastika einai epanalipsi ton formulon epi kamposes selides. mporei omos h apanalipsi na 
    # ginetai kai se mish selida. dhladh mia sthlh na einai variation 1 kai allh mia na einai variation 2
    # ap oti fainetai, ta variations uparxoun mono sto vertical format.kalutera na to afisoume anoixto to
    # endexomeno gia na mhn ksanagrafoume


@dataclass
class ParagraphSection(Paragraph):
    numberOfParagraphsPerParagraphSection: int


@dataclass
class Unit(ParagraphSection):
    numberOfParagraphSectionsPerUnit: int


@dataclass
class Chapter(Unit):
    numberOfUnitsPerChapter: int


@dataclass
class Book(Chapter):
    numberOfChapters: int


def generateParagraph(formulaeList, format):
    for formula in formulaeList.formulae:
        #print(formula.__class__.__name__)
        print("--------------------------------------------------------------")
        print(format)
        print("**************************************************")
        #print(formula)

        # for chord in formula.chords:
        #     print(chord)



def generatePart(formulaList, evolutions, part, format):

    if part.__class__.__name__ == "Book":
        pass
    elif part.__class__.__name__ == "Chapter":
        pass
    elif part.__class__.__name__ == "Unit":
        pass
    elif part.__class__.__name__ == "ParagraphSection":
        pass
    elif part.__class__.__name__ == "Paragraph":
        generateParagraph(formulaList, format)



    # 1. generate parts
    # 2. headers
    # 3. apply evolutions
    # 4. add format in the end of the part
    # 5. format is limited to page
    # 6. custom evo
    # 7. arrow evo
    # 8. book variations
    # 9. continue process/extend book
    # 10. render
    # 11. unit auto page with one measure of every paragraph
    # 12. complete the book
    # 13. make the ui
    # 14. finish the repo/setup file

# customEvolutions = CustomEvolution(evolutions=None, arrowEvolutions=None)
# arrowEvolution1 = ArrowEvolution(chordNumber=1)
# arrowEvolution2 = ArrowEvolution(chordNumber=9)
# totalArrowEvolutions = TotalArrowEvolutions([arrowEvolution1, arrowEvolution2])


################################################################################
# NOMIZO PREPEI NA PANE STO MAIN TOY MODEL AYTA APO KATO h ston controller

part1 = Paragraph(variationsNumber=1,
             numberOfVariationPages=0.5)

# part2 = ParagraphSection(numberOfParagraphsPerParagraphSection=10,
#              variationsNumber=0,
#              numberOfVariationPages=0.5)

# part3 = Unit(numberOfParagraphSectionsPerUnit=9,
#              numberOfParagraphsPerParagraphSection=10,
#              variationsNumber=0,
#              numberOfVariationPages=0.5)

# part4 = Chapter(numberOfUnitsPerChapter=8,
#              numberOfParagraphSectionsPerUnit=9,
#              numberOfParagraphsPerParagraphSection=10,
#              variationsNumber=0,
#              numberOfVariationPages=0.5)

# part5 = Book(numberOfChapters=7,
#              numberOfUnitsPerChapter=8,
#              numberOfParagraphSectionsPerUnit=9,
#              numberOfParagraphsPerParagraphSection=10,
#              variationsNumber=0,
#              numberOfVariationPages=0.5)



partGeneration = generatePart(formulaList1, evolution1, part1, format1)












# # formula2 = Formula([chord4, chord3, chord2, chord1])
# # formula3 = Formula([chord3, chord3, chord3, chord3])
# # formula4 = Formula([chord2, chord1, chord2, chord1])

# variation1 = Variation([formula1, formula2, formula3, formula4])
# # variation2 = Variation([formula2, formula2, formula2, formula2])
# # variation3 = Variation([formula4, formula3, formula3, formula1])
# # variation4 = Variation([formula4, formula1, formula1, formula1])
# paragraph1 = Paragraph([variation1, variation2])
# paragraph2 = Paragraph([variation3, variation4])
# paragraph3 = Paragraph([variation3, variation4, variation4, variation4, variation4, variation4])
# paragraph4 = Paragraph([variation3, variation4, variation2, variation2, variation2])
# unit1 = Unit([paragraph1, paragraph1, paragraph1])
# unit2 = Unit([paragraph2, paragraph2, paragraph2, paragraph2])
# unit3 = Unit([paragraph3, paragraph3, paragraph3, paragraph3, paragraph3])
# unit4 = Unit([paragraph4, paragraph4, paragraph4, paragraph4, paragraph4, paragraph4])
# chapter1 = Chapter([unit1, unit2, unit3, unit3])
# chapter2 = Chapter([unit4, unit3, unit2, unit1])
# book = Book(stringNumber=6, title="First Book", subtitle="test1", chapters= [chapter1, chapter2])







# print(book)
# print(bookFormat)
# print(serialNoteNumber.currentNoteNumbers)
# print(customSerialNoteNumberList)
# print(evolutions)
# print(customEvolutions)