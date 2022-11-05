# Desafio CRUD : Crie uma Classe chamada de OngAnimal. O seu
# construtor irá receber apenas um atributo (a lista) A lista deve ser criada
# vazia e deverá criá-la quando for instanciar o objeto. Crie 4 métodos,
# estes são: cadastrar, alterar, pesquisar e remover. Para cadastrar um
# animal, deverá receber os dados dos usuários, ou seja, através dos
# inputs. Os dados são: nome do animal, raça, peso.

#  O método cadastrar irá receber esses dados e adicionar
# dentro de uma lista, comando append.
#  O método alterar deverá alterar esses dados de acordo
# com o que o usuário pedir, deve retornar o dado alterado e
# o restante da lista.
#  O método pesquisar deverá retornar todos os dados da
# lista.

#  O método remover deverá deletar os dados que o usuário
# pedir. Deve retornar a lista atualizada.

class OngAnimal:

    def __init__(self, lista):
        self.lista = lista

    def cadastrar(self):
        nome = input("digite seu nome: ")
        raca = input("Digite a raça do seu: ")
        peso = int(input("Digite o peso do seu cao: "))
        self.lista.append(peso)
        self.lista.append(raca)
        self.lista.append(nome)
    

    def alterar(self):
        dado = input("qual dado deseja alterar? ")

        if dado in self.lista:
            posicao = self.lista.index(dado)
            modificacao = input("coloque a modificação: ")
            self.lista[posicao] = modificacao
        else:
            print("ele não está na lista")

    def pesquisar(self):
        print(self.lista)

    def remover(self):
        dado = int(input('qual dado você quer remover: '))

        if dado in self.lista:
            posicao = self.lista.index(dado)
            del(self.lista[posicao])
        else:
            print("não está na lista")


lista = []
object = OngAnimal(lista)
object.cadastrar()
object.alterar()
object.remover()