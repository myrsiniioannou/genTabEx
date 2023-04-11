from model import *

def testController():
    print("CONTROLLER FUNCTION 1")


# def initializeFormula():
#     return model.Formula(chords=[])


# def runTEST():

#     # AYTA THA GINONTAI STO MAIN FILE
#     formula = model.Formula(chords=[])

#     chord1 = model.Chord(duration=model.Duration.EIGHTH, accent=True, articulation=model.Articulation.DOWN)
#     chord2 = model.Chord(duration=model.Duration.SIXTEENTH,
#                 accent=False,
#                 articulation=model.Articulation.UP,
#                 box=True,
#                 header=[model.Fingering.P, model.Fingering.I, model.Fingering.I],
#                 note=[model.Note(noteOnString=1, string=6),model.Note(noteOnString=2, string=5)],
#                 stringFingering=model.StringFingering(string=3, fingering=model.Fingering.I),
#                 slur=model.Slur(start=True, end=False, string=3)
#                 )
#     chord3 = model.Chord(duration=model.Duration.HALF,
#                 accent=False,
#                 articulation=model.Articulation.DOWN,
#                 box=True,
#                 header=[model.Fingering.A, model.Fingering.A, model.Fingering.M],
#                 noteSymbol=model.NoteSymbol(string=2),
#                 stringfingeringWithNote=model.StringFingeringWithNote(string=4, fingering=model.Fingering.A, note=6),
#                 slur=Slur(start=False, end=True, string=3)
#                 )
#     chord4 = model.Chord(duration=model.Duration.QUARTER,
#                 articulation=model.Articulation.UP,
#                 header=[model.Fingering.I, model.Fingering.A, model.Fingering.M],
#                 stringfingeringWithNote=model.StringFingeringWithNote(string=2, fingering=model.Fingering.P, note=8),
#                 triplet=model.Triplet.FIRST
#                 )


#     formula.addChordToFormula(chord1)
#     print(formula)
#     print("----------------------")
#     formula.addChordToFormula(chord2)
#     print(formula)
#     print("----------------------")
#     formula.addChordToFormula(chord3)
#     print(formula)


if __name__ == '__main__':
    print("RUN FROM CONTROLLER")

