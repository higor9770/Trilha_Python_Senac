from tkinter import*
import tkinter as tk
from turtle import right

class Janela_Principal:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('Minha primeira janela')
        self.janela['background'] = 'lightblue'
        self.janela.geometry('750x500+550+150')

        self.nome1 = tk.Label(self.janela, text= 'Label1')
        self.nome2 = tk.Label(self.janela, text= 'Label2')
        self.nome1.grid(row=0, column=0)
        self.nome2.grid(row=1, column=0)

        self.campo1  = tk.Entry(self.janela)
        self.campo2  = tk.Entry(self.janela)
        self.campo1.grid(row=0, column=1)
        self.campo2.grid(row=1, column=1)

    def clique(self):
        self.nome1['text'] = self.campo1.get()

janela = tk.Tk()
objeto = Janela_Principal(janela)
janela.mainloop()