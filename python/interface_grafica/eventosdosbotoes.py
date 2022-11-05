from tkinter import *
import tkinter as tk
from tkinter import messagebox


class teste:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('400x200+500+200')

        self.label = tk.Label(self.janela, text = "abrir caixa", relief = 'raised')
        self.label.pack(pady=20)
        self.label.bind('<Button-1>', self.resposta)

    def resposta(self, event):
        messagebox.askquestion('olá mundo', 'confirmado com sucesso')


janela = tk.Tk()
object = teste(janela)
janela.mainloop()