from tkinter import *
import tkinter as tk


class Janela_Principal:

    def __init__(self, janela):

        self.janela = janela
        self.nome = tk.Label(self.janela, fg='#6A69F5', text='Selecione um estado')
        self.nome.pack()

        self.quadro = tk.Frame(self.janela, bg="green")

        self.barraLateral = tk.Scrollbar(self.quadro, orient=VERTICAL)

        self.lista = tk.Listbox(self.quadro, width=30, height=5, yscrollcommand=self.barraLateral.set)

        self.barraLateral.config(command=self.lista.yview)
        self.barraLateral.pack(side=RIGHT, fill=Y)

        self.quadro.pack()
        self.lista.pack(pady=10)

        self.botao = tk.Button(self.janela, width=10, text="avançar", command=self.avancar)
        self.botao.pack(pady=10)

        self.resultado = tk.Label(self.janela, width=10, text='')
        self.resultado.pack(pady=10)

        self.minhaLista = ['sp', 'Rj', 'pb', 'pe', 'sp', 'rj', 'mg', 'al']

        for item in self.minhaLista:
            self.lista.insert(END, item)

        self.imagem = tk.PhotoImage(file='image.png')
        self.recebe = tk.Label(self.janela, image=self.imagem)
        self.recebe.pack()

    def avancar(self):
        self.resultado['text'] = self.lista.get(ANCHOR)


janela = tk.Tk()
objeto = Janela_Principal(janela)
janela.mainloop()