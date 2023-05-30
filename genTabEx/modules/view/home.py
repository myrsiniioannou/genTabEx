import tkinter as tk
from dataclasses import dataclass, field


@dataclass
class GUI:
    root =  tk.Tk()
    root.geometry("800x600")
    root.title("genTabEx")
    root.mainloop()

if __name__ == '__main__':
    print("run from home file in view directory")