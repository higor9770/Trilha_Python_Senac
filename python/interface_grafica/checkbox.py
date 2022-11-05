from re import I
from tkinter import *
import tkinter as tk


class teste:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('400x200+500+200')

        self.variavel1 = tk.IntVar()

        self.marcar = tk.Checkbutton(self.janela, text="opção 1", variable=self.variavel1)
        self.marcar.pack()

        self.variavel2= tk.IntVar()

        self.marcar2 = tk.Checkbutton(self.janela, text="opção 2", variable=self.variavel2)
        self.marcar2.pack()

        self.botao = tk.Button(self.janela, text = "selecionar", command=self.minhaFuncao)
        self.botao.pack()

        self.resposta1 = tk.Label(self.janela, text='')
        self.resposta1.pack()

        self.resposta2 = tk.Label(self.janela, text='')
        self.resposta2.pack()
    
    def minhaFuncao(self):
        if self.variavel1.get() == 1:
            self.resposta1['text'] = "Opção 1 selecionada"
        else:
            self.resposta1['text'] = ''
        
        if self.variavel2.get() == 1:
            self.resposta2['text'] = 'Opção 2 selecionada'
        else:
            self.resposta2['text'] = ''


janela = tk.Tk()
object = teste(janela)
janela.mainloop()