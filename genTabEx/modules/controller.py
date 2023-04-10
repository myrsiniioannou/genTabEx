from model import *


def initializeBook(stringNumber, title, subtitle, chapters):
    pass


def initializeBookExtention(pathToBook):
    pass


def initializeBookVariation(pathToBook):
    pass



# @dataclass
# class Chord:
#     duration: Duration
#     accent: Optional[bool] = False
#     articulation: Optional[Articulation] = None
#     box: Optional[bool] = False
#     header: Optional[Fingering] = field(default_factory=list)# if there are a lot of header fingerings like ppp then the str could be more than 1 character long
#     note: Optional[Note] = None
#     noteSymbol: Optional[NoteSymbol] = None
#     stringFingering: Optional[StringFingering] = None
#     stringfingeringWithNote: Optional[StringFingeringWithNote] = None
#     slur: Optional[Slur] = None
#     triplet: Optional[Triplet] = None


# @dataclass
# class StringFingering:
#     string: int
#     fingering: Fingering

if __name__ == '__main__':
    chord = Chord(duration = Duration.SIXTEENTH, header= ["ppp"], note= Note(noteOnString = 1, string = 3),
                  stringFingering= StringFingering(2, Fingering.A))