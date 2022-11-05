from tkinter import *
import tkinter as tk
 
class senac:
 
    def __init__(self, janela):
        
        self.janela = janela
        self.janela.title('Cadastro de Salas')  # Trocar o título da janela
        #self.janela.iconbitmap('icone.ico')  # Verificar se tem o ícone no seu arquivo
        self.janela.geometry('1440x750+50+10')
        self.janela['bg'] = '#F5F5F5'
        self.janela.resizable(width=False, height=False)
 
        self.label_cima = tk.Label(self.janela, bg='#004AAD')
        self.label_cima.place(relx=0, relwidth=1, relheight=0.08, rely=0)
        self.label_baixo = tk.Label(self.janela, bg='#004AAD')
        self.label_baixo.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)
       
        self.botaoSalas = tk.Button(self.janela, text='SALAS', font='12', fg='black', bg='orange', width=10, relief=FLAT)
        self.botaoSalas.place(y = 505, x = 530)
        self.botaoProfs = tk.Button(self.janela, text='PROFESSORES', font='12', fg='black', bg='orange', width=15, relief=FLAT)
        self.botaoProfs.place(y = 505, x = 670)
 
        self.label = tk.Label(self.janela, font = 'Arial 12 bold', bg = '#F5F5F5', text = 'Olá, Administrador')
        self.label.place(y=425, x=595)
 
        self.imagem = tk.PhotoImage(file='logo 1.png')
        self.recebe = tk.Label(self.janela, image=self.imagem, bg = '#F5F5F5')
        self.recebe.place(y= 150, x= 525)
 
janela = tk.Tk()
objeto = senac(janela)
janela.mainloop()