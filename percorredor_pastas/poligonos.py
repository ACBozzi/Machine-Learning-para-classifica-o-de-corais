from tkinter import *
import tkinter as tk

class Application():
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Widget 1")
        self.msg.pack()

        my_canvas = Canvas(window, width= 200, height= 200, background= 'white')

window = tk.Tk()
#window.title("Desenhador de Poligonos")
Application(master=window)
window.mainloop
