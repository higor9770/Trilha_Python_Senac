""" Utilize o comando padx e pady para dar espaçamentos dentro do
elemento. Replique essa interface: """
from tkinter import *
import tkinter as tk

class atvd3: 

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('300x200+550+100')
        self.janela ['background'] = 'orange'


        self.label = tk.Label(self.janela, height= 10, font = 'Arial 12 bold', bg = 'lightblue', text = 'horizontal', cursor = 'heart', relief = 'sunken' )
        self.label.pack(ipadx = 30, padx = 10, pady= 20)

        self.label = tk.Label(self.janela, height= 10, font = 'Arial 12 bold', bg = 'lightblue', text = 'vertical', cursor = 'heart', relief = 'sunken' )
        self.label.pack(ipadx= 1, padx = 20, pady = 20, ipady = 60)

janela = tk.Tk()
objeto = atvd3(janela)
janela.mainloop()