# Posicionamento de Labels. Execute com o comando de
# posicionamento pack() e utilize o argumento side para replicar esse
# modelo de interface. Use 4 Labels.
from tkinter import *
import tkinter as tk
from turtle import right


class atvd3:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('300x200+550+100')
        self.janela ['background'] = 'orange'


        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightblue', text = 'label' )
        self.label.pack(side = LEFT)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightblue', text = 'label' )
        self.label.pack(side= RIGHT)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightblue', text = 'label' )
        self.label.pack(side= BOTTOM)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightblue', text = 'label' )
        self.label.pack(side = TOP)
        
janela = tk.Tk()
objeto = atvd3(janela)
janela.mainloop()