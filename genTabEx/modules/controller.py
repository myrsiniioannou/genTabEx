#from model import *


# ο controller αποδέχεται τις εισαγωγές του χρήστη και αναθέτει την αναπαράσταση δεδομένων στο view





import pickle



# with open("data/current-serial-note-number.pkl", 'wb') as f:  # open a text file
#     pickle.dump(248, f) # serialize the list


with open("data/current-serial-note-number.pkl", 'rb') as f:
    b = pickle.load(f)

print(b)

# chord1 = Chord(duration=Duration.EIGHTH, accent=True, articulation=Articulation.DOWN)
# chord2 = Chord(duration=Duration.SIXTEENTH,
#             accent=False,
#             articulation=Articulation.UP,
#             box=True,
#             header=[Fingering.P, Fingering.I, Fingering.I],
#             note=[Note(noteOnString=1, string=6),Note(noteOnString=2, string=5)],
#             stringFingering=StringFingering(string=3, fingering=Fingering.I),
#             slur=Slur(start=True, end=False, string=3)
#             )

# chord3 = Chord(duration=Duration.HALF,
#             accent=False,
#             articulation=Articulation.DOWN,
#             box=True,
#             header=[Fingering.A, Fingering.A, Fingering.M],
#             noteSymbol=NoteSymbol(string=2),
#             stringfingeringWithNote=StringFingeringWithNote(string=4, fingering=Fingering.A, note=6),
#             slur=Slur(start=False, end=True, string=3)
#             )
# chord4 = Chord(duration=Duration.QUARTER,
#             articulation=Articulation.UP,
#             header=[Fingering.I, Fingering.A, Fingering.M],
#             stringfingeringWithNote=StringFingeringWithNote(string=2, fingering=Fingering.P, note=8),
#             triplet=Triplet.FIRST
#             )



# formula = Formula()
# formula.addChordToFormula(chord1)
# formula.addChordToFormula(chord2)
# formula.addChordToFormula(chord3)
# formula.addChordToFormula(chord4)
# print("LENGTH OF CHORDS = ", len(formula.chords))
# formula.multiply(16)
# print("LENGTH OF CHORDS = ", len(formula.chords))








if __name__ == '__main__':
    pass

