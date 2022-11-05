from tkinter import *
import tkinter as tk
from tkinter.ttk import *

class teste: 

        def __init__(self, janela):
            self.janela = janela
            self.janela.title('teste')
            self.janela.geometry('400x200+500+200')
            self.janela ['background'] = '#E3FFBD'

            self.passo = tk.Label(self.janela, text = "0%", bg = '#E3FFBD' )
            self.passo.pack()

            self.barra = Progressbar(self.janela, length = 300)
            self.barra['value'] = 0
            self.barra.pack()

            self.botao = tk.Button(self.janela, text='avançar', command=self.progressao)
            self.botao.pack()

        def progressao(self):
            self.barra['value'] = self.barra['value'] + 10
            self.passo['text'] = str(self.barra['value']) + '%'

            if self.barra ['value'] >= 100:
                self.passo ['text'] = '100%'
                self.passo ['text'] = 'contagem finalizada'

janela = tk.Tk()
object = teste(janela)
janela.mainloop()