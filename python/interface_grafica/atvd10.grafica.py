from tkinter import *
import tkinter as tk
from tkinter import messagebox
from webbrowser import BackgroundBrowser


class teste:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('400x200+500+200')
        self.janela ['background'] = 'lightblue'

        self.label1 = tk.Label(self.janela, text = "informação", relief = 'raised')
        self.label1.pack(pady=20)
        self.label1.bind('<Button-1>', self.informacao)

        self.label2 = tk.Label(self.janela, text = "aviso", relief = 'raised')
        self.label2.pack(pady=20)
        self.label2.bind('<Button-1>', self.aviso)

        
        self.label3 = tk.Label(self.janela, text = "erro", relief = 'raised')
        self.label3.pack(pady=20)
        self.label3.bind('<Button-1>', self.erro)

        
        self.label4 = tk.Label(self.janela, text = "pergunta", relief = 'raised')
        self.label4.pack(pady=20)
        self.label4.bind('<Button-1>', self.pergunta)

        
        self.label5 = tk.Label(self.janela, text = "dúvida", relief = 'raised')
        self.label5.pack(pady=20)
        self.label5.bind('<Button-1>', self.duvida)


    def informacao(self, event):
        messagebox.showinfo('caixa de informação')
    
    def aviso(self, event):
        messagebox.showwarning('caixa de informação')

    def erro(self, event):
        messagebox.showerror('caixa de informação')

    def pergunta(self, event):
        messagebox.askquestion('caixa de informação')

    def duvida(self, event):
        messagebox.askyesnocancel('caixa de informação')


janela = tk.Tk()
object = teste(janela)
janela.mainloop()