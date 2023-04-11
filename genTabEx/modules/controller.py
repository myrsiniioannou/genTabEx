from model import *

# AYTA THA GINONTAI STO MAIN FILE
formula = Formula(chords=[])

chord1 = Chord(duration=Duration.EIGHTH, accent=True, articulation=Articulation.DOWN)
chord2 = Chord(duration=Duration.SIXTEENTH,
               accent=False,
               articulation=Articulation.UP,
               box=True,
               header=[Fingering.P, Fingering.I, Fingering.I],
               note=[Note(noteOnString=1, string=6),Note(noteOnString=2, string=5)],
               stringFingering=StringFingering(string=3, fingering=Fingering.I),
               slur=Slur(start=True, end=False, string=3)
               )
chord3 = Chord(duration=Duration.HALF,
               accent=False,
               articulation=Articulation.DOWN,
               box=True,
               header=[Fingering.A, Fingering.A, Fingering.M],
               noteSymbol=NoteSymbol(string=2),
               stringfingeringWithNote=StringFingeringWithNote(string=4, fingering=Fingering.A, note=6),
               slur=Slur(start=False, end=True, string=3)
               )
chord4 = Chord(duration=Duration.QUARTER,
               articulation=Articulation.UP,
               header=[Fingering.I, Fingering.A, Fingering.M],
               stringfingeringWithNote=StringFingeringWithNote(string=2, fingering=Fingering.P, note=8),
               triplet=Triplet.FIRST
               )


formula.addChordToFormula(chord1)
print(formula)
print("----------------------")
formula.addChordToFormula(chord2)
print(formula)
print("----------------------")
formula.addChordToFormula(chord3)
print(formula)
print("----------------------")


if __name__ == '__main__':
    pass
