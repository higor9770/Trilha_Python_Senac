from re import I
from tkinter import *
import tkinter as tk


class teste:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('400x200+500+200')

        self.var = tk.IntVar()

        self.radio = tk.Radiobutton(self.janela, text = "opção 1", variable=self.var, value=1)
        self.radio.pack()


        self.radio2 = tk.Radiobutton(self.janela, text = "opção 2", variable=self.var, value=2)
        self.radio2.pack()

        self.radio3 = tk.Radiobutton(self.janela, text = "opção 3", variable=self.var, value=3)
        self.radio3.pack()

        self.botao = tk.Button(self.janela, text = "selecionar", command=self.imprimir)
        self.botao.pack()

        self.resposta = tk.Label(self.janela, text = '')
        self.resposta.pack()

    def imprimir(self):
        self.selecionado = "você selecionou a opção" +str(self.var.get())
        self.resposta['text'] = self.selecionado

janela = tk.Tk()
object = teste(janela)
janela.mainloop()