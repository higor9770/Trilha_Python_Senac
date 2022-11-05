from tkinter import *
import tkinter as tk


class Janela_Principal:

    def __init__(self, janela):

        self.janela = janela
        self.info = tk.Label(self.janela, text = 'Soma')
        self.info.pack()

        self.numero1 = tk.Label(self.janela, text = 'Numero 1: ')
        self.numero1.pack()
        self.campo1 = tk.Entry(self.janela, width=15)
        self.campo1.pack()

        self.numero2 = tk.Label(self.janela, text = 'Numero 2: ')
        self.numero2.pack()
        self.campo2 = tk.Entry(self.janela, width=15)
        self.campo2.pack()
  
        self.botao = tk.Button(self.janela, text='soma', width=20, command=self.soma)
        self.botao.pack(pady=20)

        self.resultado = tk.Label(self.janela, width=500, height=2)
        self.resultado.pack()
    
    def soma(self):
        try: 
            n1 = int(self.campo1.get())
            n2 = int(self.campo2.get())
            self.resultado['text'] = n1 + n2
        except ValueError as erro:
            self.resultado['text'] = 'só aceitamos números!'

janela = tk.Tk()
objeto = Janela_Principal(janela)
janela.mainloop()