class Cruds:
    def __init__(self, lista):
        self.lista = lista
    
    """ adicionar """
    def adicionar(self):
        for i in range(4):
            nome = str(input('nome: '))
            self.lista.append(nome)
        print(self.lista)

    """ inserir """
    def inserir(self):
        posicao = int(input('Qual posição você quer inserir um dado: '))
        modificacao = input('Coloque a modificação: ')
        self.lista.insert(posicao, modificacao)
        print(self.lista)
        
    def alterar(self):
        posicao = int(input('Qual a posição você quer alterar uma dado: '))
        modificacao = input('coloque a modificação: ')
        self.lista[posicao] = modificacao
        print(self.lista)

    def pesquisar(self):
        posicao = int(input('Qual posição deseja visualizar: '))
        print(self.lista[posicao])
        print(self.lista)

    def remover(self):
        posicao = int(input('qual posição vai remover: '))
        del (self.lista[posicao])
        print(self.lista)

    def alterar2(self):
        palavra = input("qual dado deseja alterar? ")
        if palavra in self.lista:
            posicao = self.lista.index(palavra)
            modificacao = input("Coloque a modificação: ")
            self.lista[posicao] = modificacao
        else: 
            print("Não está na lista!")
        print(self.lista)

    
lista = []
object = Cruds(lista)
object.adicionar()
object.inserir()
object.alterar()
object.pesquisar()
object.remover()
object.alterar2()
