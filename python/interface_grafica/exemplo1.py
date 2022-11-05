from tkinter import*
import tkinter as tk

class Janela_Principal:

    def __init__(self, janela):

        self.janela = janela
        self.janela.title("Minha primeira janela")
        self.janela['background'] = '#8DCEF2'
        self.janela.iconbitmap('interface_grafica\coracao.ico')
        self.janela.geometry('500x300+540+100')

        self.nome1 = tk.Label(self.janela, fg='#6A69F5', font =  'verdana 12 bold', text = 'isso é uma label', height= 3, width = 15, cursor = 'dot', relief = 'groove')
        self.nome1.place(x=65, y=10)
        self.entrada = tk.Entry(self.janela, width=20)
        self.entrada.place(x = 90, y = 90)
        self.botao = tk.Button(self.janela, fg='black', background='#F7E89C',  text = "Botao", command = self.clique)
        self.botao.place(x = 130, y = 140)
        self.nome2 = tk.Label(self.janela, fg='#6A69F5', font =  'verdana 12 bold', text = 'isso é uma label', height= 3, width = 15, cursor = 'dot', relief = 'groove')
        self.nome2.place(x=70, y=190)

        self.frame = tk.Frame(self.janela, bg="orange", width=100, height=100)
        self.frame.pack()

        #pack -- coloca tudo no meio
        #place -- posiciona a partir do eixo y e x
        #grid -- posiciona o elemento por linhas e colunas

        self.scrollbar = tk.Scrollbar(self.janela)
        self.scrollbar.pack(side = RIGHT, fill=Y)

    def clique(self):
        self.nome2['text'] = self.entrada.get()

janela = tk.Tk()
objeto = Janela_Principal(janela)
janela.mainloop()