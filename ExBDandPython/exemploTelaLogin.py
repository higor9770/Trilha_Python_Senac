import sqlite3
from sqlite3 import Error
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Login:
    def __init__(self,  janela, conexao):
        self.conexao = conexao
        self.janela = janela
        self.janela.title('Tabelas com TKinter')
        self.janela.geometry('800x320+150+100')
        self.usuario = tk.Label(self.janela, text='usuario')
        self.usuario.pack()

        self.campo1 = tk.Entry(self.janela)
        self.campo1.pack()

        self.senha = tk.Label(self.janela, text='senha')
        self.senha.pack()
        
        self.campo2 = tk.Entry(self.janela, show='*')
        self.campo2.pack()
        self.btInserir = tk.Button(self.janela, text='Entrar', command=self.login).pack()


    def login(self):
        c = self.conexao.cursor()
        sql = "SELECT * FROM tb_login WHERE usuario = '" + self.campo1.get() + "' AND senha = '" + self.campo2.get() + "'"
       # c.execute("SELECT * FROM tb_login WHERE usuario = ? AND senha = ?", (self.campo1.get(), self.campo2.get()))
        c.execute(sql)
        if c.fetchall():
            messagebox.showinfo('caixa de mensagem', 'Bem vindo(a)!')
        else:
            messagebox.showerror('Error', 'Senha ou email incorreto!')
        c.close()






#------------------ Fora da Classe ------------------

def conexaoBanco():
    caminho = 'C:\\Users\\Compaq\\Downloads\\ProjetoModelo\\banco\\login.db'
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
        print('Conexao aceita')
    except Error as ex:
        print('Erro de conexão:', ex)
    return conexao

janela = tk.Tk()
conexao = conexaoBanco()
objeto = Login(janela, conexao)
janela.mainloop()
conexao.close()