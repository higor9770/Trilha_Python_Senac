# Crie uma função funcionário que recebe como parâmetros, nome,
# idade, profissão. Crie uma função menu para receber os valores do
# usuário e retorne na tela as informações.


def funcionario (nome, idade, profissao):

   return  f'{nome} \n\n {idade} \n\n {profissao}'

def menu ():

    nome = str(input("digite seu nome: "))
    idade = int(input("digite sua idade: "))
    profissao = str(input("digite sua profissao: "))

    print(funcionario(nome, idade, profissao))

menu()