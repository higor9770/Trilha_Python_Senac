# Escreva uma função chamada de info que recebe dois parâmetros:
# nome e telefone e retorne esses parâmetros através do comando return
# dentro da função. Deve criar outra função chamada de menu() e a mesma
# irá receber os valores através dos inputs dos usuários.

def info(nome, telefone):

    return f'{nome}, {telefone}' # com o format para sair da tupla

def menu():

    telefone = int(input("digite seu numero de telefone: "))
    nome = str(input("digite seu nome: "))

    print(info(nome, telefone)) #você é obrigado a retornar os dois parametros
    # print(info(nome)) # ele não retorna apenas um parametro, você é obrigado a colocar os dois parametros
    # print(info(telefone)) #  ele não retorna apenas um parametro, você é obrigado a colocar os dois parametros

menu()
