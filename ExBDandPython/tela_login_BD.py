import sqlite3
from sqlite3 import Error
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#SÓ FALTA CONECTAR COM O BANCO DE DADOS
        
class Login:
    def __init__(self, janela, conexao):
        self.conexao = conexao
        self.janela_login = janela
        self.janela_login.title('Tela de Acesso')
        self.janela_login.geometry('1440x750+50+10')
        self.janela_login['bg'] = '#F5F5F5' #BOTÃO LARANJA #DE8708
        self.janela_login.resizable(False, False)

        self.label_superior = tk.Label(self.janela_login, bg='#004AAD', fg='white', font='Verdana 20 bold')
        self.label_superior.place(relx=0, relwidth=1, relheight=0.08, rely=0)

        #self.imagem = tk.PhotoImage(file=r'C:\Users\Aluno\PycharmProjects\pythonProject\Gabriel_Formacao_Python_Tarde\Código_Unificado\logosenac.png')
        #self.label_logoSenac = tk.Label(self.janela_login, image=self.imagem)
        #self.label_logoSenac.place(relx=0.44, rely=0.12, relheight=0.25, relwidth=0.18)

        self.label_login = tk.Label(self.janela_login, text='Login:', font='Inter 17 bold', bg='white')
        self.label_login.place(relx=0.30, rely=0.45, relheight=0.05, relwidth=0.06)
        self.entrada_login = tk.Entry(self.janela_login, bg='lightgray', font='Inter 17')
        self.entrada_login.place(relx=0.40, rely=0.45, relheight=0.05, relwidth=0.30)

        self.label_senha = tk.Label(self.janela_login, text='Senha:', font='Inter 17 bold', bg='white')
        self.label_senha.place(relx=0.30, rely=0.53, relheight=0.05, relwidth=0.07)
        self.entrada_senha = tk.Entry(self.janela_login, bg='lightgray', font='Inter 17', show='*')
        self.entrada_senha.place(relx=0.40, rely=0.53, relheight=0.05, relwidth=0.30)

        self.mensagem_acesso = tk.Label(self.janela_login, text='', bg='#F5F5F5', font='Verdana 16')
        self.mensagem_acesso.place(relx=0.43, rely=0.62, relheight=0.05, relwidth=0.25)

        self.botao_entrar = tk.Button(self.janela_login, text='ENTRAR', font='Inter 17 bold', fg='white', bg='#DE8708', relief=GROOVE, command=self.login)
        self.botao_entrar.place(relx=0.36, rely=0.70, relheight=0.08, relwidth=0.10)
        #self.botao_entrar.bind('<Return>', self.enter_confirmar)
        #self.botao_entrar.bind('<Any-Button>', self.clique_confirmar)

        self.botao_cadastrar = tk.Button(self.janela_login, text='CADASTRAR', font='Inter 17 bold', fg='white', bg='#004AAD', relief=GROOVE, command=self.login)
        self.botao_cadastrar.place(relx=0.58, rely=0.70, relheight=0.08, relwidth=0.15)
        #self.botao_cadastrar.bind('<Return>') receberá a função para cadastrar futuramente
        #self.botao_cadastrar.bind('<Any-Button>') receberá a função para cadastrar futuramente

        self.label_esqueci_senha = tk.Label(self.janela_login, text='Esqueci minha senha', font='Verdana 16', fg='#004AAD', bg='white')
        self.label_esqueci_senha.place(relx=0.43, rely=0.83, relheight=0.05, relwidth=0.20)
        # self.label_esqueci_senha.bind('<Return>') receberá a função para cadastrar futuramente
        # self.botao_esqueci_senha.bind('<Any-Button>') receberá a função para cadastrar futuramente

        self.label_inferior = tk.Label(self.janela_login, bg='#004AAD')
        self.label_inferior.place(relx=0, relwidth=1, relheight=0.08, rely=0.92)

    def login(self):
        c = self.conexao.cursor()
        sql = "SELECT * FROM tb_login WHERE login = '" + self.entrada_login() + "' AND senha = '" + self.entrada_senha() + "'"
       # c.execute("SELECT * FROM tb_login WHERE usuario = ? AND senha = ?", (self.campo1.get(), self.campo2.get()))
        c.execute(sql)
        if c.fetchall():
            messagebox.showinfo('caixa de mensagem', 'Bem vindo(a)!')
        else:
            messagebox.showerror('Error', 'Senha ou email incorreto!')
        c.close()

#------------------ Fora da Classe ------------------

def conexaoBanco():
    caminho = 'usar banco de dados'
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