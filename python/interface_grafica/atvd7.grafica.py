""" Teste 6 tipos de cursores nas labels, deve fazer uma label para cada
cursor, e teste os tipos de bordas nas mesmas labels. """
from tkinter import *
import tkinter as tk

class atvd3: 

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('300x200+550+100')
        self.janela ['background'] = 'orange'

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightgreen', text = 'Botão 1', cursor = 'dot', relief = 'flat' )
        self.label.place(x= 400 , y=200)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightgreen', text = 'Botão 2', cursor = 'star', relief = 'raised')
        self.label.place(x= 500 , y=200)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightgreen', text = 'Botão 3', cursor = 'mouse', relief = 'sunken' )
        self.label.place(x= 600 , y=200)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightgreen', text = 'Botão 4', cursor = 'spraycan', relief = 'groove' )
        self.label.place(x= 700 , y=200)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightgreen', text = 'Botão 5', cursor = 'pirate', relief = 'ridge' )
        self.label.place(x= 800 , y=200)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightblue', text = 'Botão 6', cursor = 'heart', relief = 'sunken' )
        self.label.place(x= 900 , y=200)



janela = tk.Tk()
objeto = atvd3(janela)
janela.mainloop()

