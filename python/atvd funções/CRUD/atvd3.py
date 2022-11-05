class pessoa:

    def __init__(self): # só definir os parametros apenas se pedir os inputs lá fora
        
        nome = (input("digite seu nome: "))
        idade = int(input("digite sua idade: "))
        altura = float(input("digite sua altura: "))
        peso = float(input("digite seu peso: "))
        self.nome = nome
        self.idade = idade
        self.alturaa = altura
        self.peso = peso

        print(nome)
        print(idade)
        print(altura)
        print(peso)

    

object = pessoa()