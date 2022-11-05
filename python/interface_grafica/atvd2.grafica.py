# 2. Crie uma interface gráfica que tenha essas características:

# Dois Labels com nome na cor preta fonte Arial 12 bold. Cor
# de fundo azul claro.
# A cor da janela é sem cor.
# Os botões são largura 10 e altura 2. A fonte verdana 12
# bold. A cor é de sua escolha.
# Cada label corresponde a um botão. Irão ficar um abaixo
# do outro.Use o pack()

from tkinter import *
import tkinter as tk


class atvd2:

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('300x200+550+100')
        self.janela ['background'] = 'orange'

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightblue', text = 'label' )
        self.label.pack(pady=20)
        self.botao = tk.Entry(self.janela, width=15, font = 'verdana 12 bold')
        self.botao.pack()

        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = 'lightblue', text = 'label' )
        self.label.pack(pady=20)
        self.botao = tk.Entry(self.janela, width=15, font = 'verdana 12 bold')
        self.botao.pack()

janela = tk.Tk()
objeto = atvd2(janela)
janela.mainloop()