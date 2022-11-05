""" Com base nessa imagem a seguir deve fazer as seguintes
características: Criar dois labels para receber nome e idade, e ao clicar
no botão, retornar no label de resposta. Lembre-se de criar a função
para receber essa ação e retornar no botão. Não esqueça do command
para o método ser invocado.Use o gerenciador place(). """

from tkinter import *
import tkinter as tk

class atvd3: 

    def __init__(self, janela):
        self.janela = janela
        self.janela.title('teste')
        self.janela.geometry('300x200+550+100')
        self.janela ['background'] = 'orange'


        self.label1 = tk.Label(self.janela, width = 5, font = 'Arial 12 bold', bg = 'orange', text = 'NOME:', cursor = 'heart')
        self.label1.place(x= 525 , y=200) #O que vai indicar na tela para o usuário
        self.label2 = tk.Label(self.janela, width = 5, font = 'Arial 12 bold', bg = 'orange', text = 'IDADE:', cursor = 'heart')
        self.label2.place(x= 525 , y=250)

        self.entrada1 = tk.Entry(self.janela, width=10, font = 'verdana 12 bold') #Entrada de dados
        self.entrada1.place(x= 600 , y=200)
        self.entrada2 = tk.Entry(self.janela, width=10, font = 'verdana 12 bold')
        self.entrada2.place(x= 600 , y=250)

        self.botao = tk.Button(self.janela, fg='black', background='#F7E89C',  text = "selecionar", command = self.clique)
        self.botao.place(x = 650, y = 300) # Botão

        self.resultado = tk.Label(self.janela, width=10, text='')
        self.resultado.place(x = 750, y = 201)

        self.resultado2 = tk.Label(self.janela, width=10, text='')
        self.resultado2.place(x = 750, y = 251)
        
    def clique(self):
        self.resultado['text'] = self.entrada1.get()
        self.resultado2['text'] = int(self.entrada2.get())


janela = tk.Tk()
objeto = atvd3(janela)
janela.mainloop()