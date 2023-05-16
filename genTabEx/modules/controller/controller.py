import sys
sys.path.append('modules/model')
sys.path.append('modules/view')
from format import *
from domain_model import *
from evolutions import *
from render import *
from serial_note_numbers import *

# ο controller αποδέχεται τις εισαγωγές του χρήστη και αναθέτει την αναπαράσταση δεδομένων στο view






serialNoteNumber = SerialNoteNumber(serialNumberRepeatingType=SerialNumberRepeatingType.firstCharacterDoubling,
                                    twelveNoteLengthSerialNotes= True)

customSerialNoteNumberList = CustomSerialNoteNumberList(serialNoteNumberList = None)


chord1 = Chord(duration=Duration.EIGHTH, accent=False, articulation = Articulation.UP, box=False, header=[Fingering.A, Fingering.P],
               note = Note(noteOnString=0, string=3), noteSymbol= NoteSymbol(string=3), stringFingering = StringFingering(fingering=Fingering.I,string=6), stringfingeringWithNote=False,
               slur= Slur(start=True, string=2, end=False), triplet=Triplet.FIRST)
chord2 = Chord(duration=Duration.HALF, accent=True, articulation = Articulation.DOWN, box=True, header=[Fingering.M, Fingering.I],
               note = Note(noteOnString=0, string=4), stringFingering = StringFingeringWithNote(string=4, fingering=Fingering.A, note=5),
               triplet=Triplet.SECOND)
chord3 = Chord(duration=Duration.SIXTEENTH, accent=False, articulation = Articulation.DOWN, box=False, header=[Fingering.A, Fingering.P],
               note = Note(noteOnString=0, string=3), noteSymbol= NoteSymbol(string=6),
               stringFingering = StringFingering(fingering=Fingering.A,string=4), stringfingeringWithNote=False,
               slur= Slur(start=False, string=5, end=True), triplet=Triplet.THIRD)
chord4 = Chord(duration=Duration.WHOLE, accent=True, box=False, header=[Fingering.M, Fingering.M],
               note = Note(noteOnString=0, string=6), stringFingering = StringFingering(fingering=Fingering.I,string=6), stringfingeringWithNote=False,
               slur= Slur(start=True, string=2, end=False), triplet=Triplet.FIRST)





formula1 = Formula(chords=[chord1, chord2, chord3, chord4])
formula1.multiply(3)
formula2= Formula(chords=[chord2, chord2, chord2, chord2])
formula2.multiply(3)

formulaList1 = FormulaList(formulae=[formula1, formula2])

evolution1 = Evolution(type=EvolutionType.stringAscending, fingeringNotNote= True, chordNumber =[1,5],
                       string=2, stringStep=1)



format1 = Format(stringNumber=6,
                 title="test",
                 subtitle=" 1",
                 numberOfRows=6,
                 numberOfColumns=2,
                 paragraphOrderType=ParagraphOrderType.paragraphNumberFirst,
                 headerRepeatFormat=HeaderRepeatFormat(rows=1,columns=2),
                 formulaFormat=FormulaFormat(horizontalFormat=False, formulaLetterVisibility=True),
                 beams={6:BeamType.doubleLine, 6:BeamType.singleLine},
                 numberOfFormulaRepeats=[1,2]
                 )

print(format1)      

# @dataclass
# class BeamType(int, Enum):
#     defaut = 1
#     singleLine = 2
#     doubleLine = 3

# @dataclass
# class Beam():
#     chord: int #minus one for all the chords in formula
#     beamType: BeamType

    # numberOfFormulaRepeats: int = field(default_factory=list) # each element is the number that each formula should repeat
    # beams: BeamType = field(default_factory=list) # list of all the chords and their 
                 
                 
                 
                 
                 
                 




if __name__ == '__main__':
    print("run from CONTROLLER file in CONTROLLER directory")







# import pickle
# with open("data/current-serial-note-number-12-note-length.pkl", 'wb') as f:  # open a text file
#     pickle.dump(28, f) # serialize the list


# with open("data/current-serial-note-number-12-note-length.pkl", 'rb') as f:
#     b = pickle.load(f)

# print(b)









if __name__ == '__main__':
    pass

