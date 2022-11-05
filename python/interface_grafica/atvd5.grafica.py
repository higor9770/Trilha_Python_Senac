# Utilize o gerenciador place() e Reproduza essa linda pirâmide de botões
from tkinter import *
import tkinter as tk

class atvd3:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('300x200+550+100')
        self.janela ['background'] = 'orange'



        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 600 , y=240)

        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 650 , y=240)

        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 700 , y=240)

        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 619 , y=218, width=60)

        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 679 , y=218, width=60)

        self.botao = tk.Entry(self.janela, width=5, font = 'verdana 12 bold')
        self.botao.place(x= 650 , y=196)

janela = tk.Tk()
objeto = atvd3(janela)
janela.mainloop()