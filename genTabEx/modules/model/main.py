from domain_model import *
from evolutions import *
from format import *
from render import *
from serial_note_numbers import *







chord1 = Chord(duration=Duration.EIGHTH, accent=False, articulation = Articulation.UP, box=False, header=[Fingering.A, Fingering.P],
               note = Note(noteOnString=1, string=3), noteSymbol= NoteSymbol(string=3), stringFingering = StringFingering(fingering=Fingering.I,string=6), stringfingeringWithNote=False,
               slur= Slur(start=True, string=2, end=False), triplet=Triplet.FIRST)
chord2 = Chord(duration=Duration.HALF, accent=True, articulation = Articulation.DOWN, box=True, header=[Fingering.M, Fingering.I],
               note = Note(noteOnString=2, string=4), stringFingering = StringFingeringWithNote(string=4, fingering=Fingering.A, note=5),
               triplet=Triplet.SECOND)
chord3 = Chord(duration=Duration.SIXTEENTH, accent=False, articulation = Articulation.DOWN, box=False, header=[Fingering.A, Fingering.P],
               note = Note(noteOnString=1, string=3), noteSymbol= NoteSymbol(string=6),
               stringFingering = StringFingering(fingering=Fingering.A,string=4), stringfingeringWithNote=False,
               slur= Slur(start=False, string=5, end=True), triplet=Triplet.THIRD)
chord4 = Chord(duration=Duration.WHOLE, accent=True, box=False, header=[Fingering.M, Fingering.M],
               note = Note(noteOnString=6, string=6), stringFingering = StringFingering(fingering=Fingering.I,string=6), stringfingeringWithNote=False,
               slur= Slur(start=True, string=2, end=False), triplet=Triplet.FIRST)

formula1 = Formula([chord1, chord2, chord3, chord4])
formula2 = Formula([chord4, chord3, chord2, chord1])
formula3 = Formula([chord3, chord3, chord3, chord3])
formula4 = Formula([chord2, chord1, chord2, chord1])
variation1 = Variation([formula1, formula2, formula3, formula4])
variation2 = Variation([formula2, formula2, formula2, formula2])
variation3 = Variation([formula4, formula3, formula3, formula1])
variation4 = Variation([formula4, formula1, formula1, formula1])
paragraph1 = Paragraph([variation1, variation2])
paragraph2 = Paragraph([variation3, variation4])
paragraph3 = Paragraph([variation3, variation4, variation4, variation4, variation4, variation4])
paragraph4 = Paragraph([variation3, variation4, variation2, variation2, variation2])
unit1 = Unit([paragraph1, paragraph1, paragraph1])
unit2 = Unit([paragraph2, paragraph2, paragraph2, paragraph2])
unit3 = Unit([paragraph3, paragraph3, paragraph3, paragraph3, paragraph3])
unit4 = Unit([paragraph4, paragraph4, paragraph4, paragraph4, paragraph4, paragraph4])
chapter1 = Chapter([unit1, unit2, unit3, unit3])
chapter2 = Chapter([unit4, unit3, unit2, unit1])
book = Book(stringNumber=6, title="First Book", subtitle="test1", chapters= [chapter1, chapter2])


print(book)