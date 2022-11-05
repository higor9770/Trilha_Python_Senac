# Escreva uma função livro que irá receber quatro parâmetros: nome,
# qtdPaginas, autor e preço. Deve retornar essas informações com o
# comando print dentro da própria função. Em seguida, deve criar uma
# função menu(), o menu irá receber os inputs dos usuários. Mostrem na
# tela os resultados.


def livro(nome, qtdPaginas, autor, preco):

    print(nome)
    print(qtdPaginas)
    print(autor)
    print(preco)

def menu():

    nome = str(input("digite um nome: "))
    qtdPaginas = int(input("digite a quantidade de páginas: "))
    autor = str(input("digite o nome do autor: "))
    preco = float(input("digite o preço: "))

    livro(nome, qtdPaginas, autor, preco)

menu()

