class Cruds:
    def __init__(self, lista):
        self.lista = lista

    def menu(self):

        print("\n")
        print("="*25)
        print("Olá, Bem vindo ao plano sócio torcedor Rubro Negro!")
        print("="*25)
        print("1 - Se Cadastrar ")
        print("2 - Modificar seus dados ")
        print("3 - Visualizar seus dados ")
        print("3 - Delete seus dados")
    
        escolha = int(input("\nSelecione uma das opções: "))

        if escolha == 1:
            self.adicionar()
       
        elif escolha == 2:
            self.alterar2()
            
        elif escolha == 3:
            self.pesquisar()

        elif escolha == 4:
            self.remover()

        elif escolha == 0:
            self.alterar2()
        else:
            print("erro!")

    
    """ adicionar """
    def adicionar(self):
        print("<<<<<< coloque seus dados >>>>>>")
        nome1 = input("\ndigite seu nome: ")
        cpf1 = str(input("\ndigite seu CPF: "))
        idade1 = str(input("\ndigite sua idade: "))
        endereco1 = str(input("\ndigite seu endereco: "))
        self.lista.append(nome1)
        self.lista.append(cpf1)
        self.lista.append(idade1)
        self.lista.append(endereco1)
        dependentes = int(input("\nQuantos dependentes deseja colocar no seu plano: "))
        for i in range(dependentes):
            nomeDep = str(input('\nNome: '))
            cpfDep = str(input("\nCPF: "))
            idadeDep = str(input("\nidade: "))
            enderecoDep = str(input("\nEndereço: "))
            self.lista.append(nomeDep)
            self.lista.append(cpfDep)
            self.lista.append(idadeDep)
            self.lista.append(enderecoDep)

        print("1- voltar ao menu")
        print("2- fim do programa")
        escolha2 = int(input("O que deseja fazer? "))
        if escolha2 == 1:
            self.menu()
        elif escolha2 == 2:
            self.final()
        else:
            print("erro")
        
    def alterar2(self):
        print(self.lista)
        palavra = str(input("qual dado deseja alterar? "))
        if palavra in self.lista:
            posicao = self.lista.index(palavra)
            modificacao = str(input("Coloque a modificação: "))
            self.lista[posicao] = modificacao
        else: 
            print("Não está na lista!")
        print(self.lista)
        
        print("1- voltar ao menu")
        print("2- fim do programa")
        escolha2 = int(input("O que deseja fazer? "))
        if escolha2 == 1:
            self.menu()
        elif escolha2 == 2:
            self.final()
        else:
            print("erro")

    def pesquisar(self):
        print(self.lista)
        print("1- voltar ao menu")
        print("2- fim do programa")
        escolha2 = int(input("O que deseja fazer? "))
        if escolha2 == 1:
            self.menu()
        elif escolha2 == 2:
            self.final()
        else:
            print("erro")

    def remover(self):
        posicao = int(input('qual posição vai remover: '))
        del (self.lista[posicao])
        print(self.lista)
        
        print("1- voltar ao menu")
        print("2- fim do programa")
        escolha2 = int(input("O que deseja fazer? "))
        if escolha2 == 1:
            self.menu()
        elif escolha2 == 2:
            self.final()
        else:
            print("erro")

    def final(self):
        print("Obrigado por usar nosso APP")

        
lista = []
object = Cruds(lista)
object.menu()
object.adicionar()
object.pesquisar()
object.alterar2()
object.remover()
object.final()