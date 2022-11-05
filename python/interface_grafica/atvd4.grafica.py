# Replique essa interface: Utilize o gerenciador place(). Utilize Label e
# Botões.

from tkinter import *
import tkinter as tk
from turtle import right

class atvd3:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('300x200+550+100')
        self.janela ['background'] = 'orange'

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'orange', text = 'Botão 1' )
        self.label.place(x= 400 , y=200)
        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 400 , y=240)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'orange', text = 'Botão 2' )
        self.label.place(x= 600 , y=200)
        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 600 , y=240)

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'orange', text = 'Botão 3' )
        self.label.place(x= 800 , y=200)
        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 800 , y=240 )

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'orange', text = 'Botão 4' )
        self.label.place(x= 1000 , y=200)
        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 1000 , y=240)

janela = tk.Tk()
objeto = atvd3(janela)
janela.mainloop()