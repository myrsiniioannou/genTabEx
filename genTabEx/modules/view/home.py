import tkinter as tk
from dataclasses import dataclass, field

# the View presents the data to the user. A View can be any kind of 
# output representation: an HTML page, a chart, a table, or even a simple text output. 
# A View should never call its own methods; only a Controller should do it.


# EDO OUSIASTIKA EMFANIZO KAI EKSAFANIZO TA DEDOMENA KAI GRAPHICS

# O CONTROLLER XEIRIZETAI THN EMFANISH AFTH KAI TRIGGAREI TO MODELO

@dataclass
class GUI:
    root =  tk.Tk()
    root.geometry("800x600")
    root.title("genTabEx")
    root.mainloop()

showGUI = GUI()