# Meu objetivo: Cria um sistema de cadastro para cadastrar o sócio torcedor do Sport Club do Recife
# e seus dependentes. Objetivo: Após o cadastro o usuário consiga atualizar os dados, visualizar,
# deletar algum dado em específico, deletar todos os dados e sair do app ao final do comando do usuário. 

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
        print("4 - Deletar dado específico ")
        print("5 - deletar todos os dados ")
        print("6 - sair do app")
    
        escolha = int(input("\nSelecione uma das opções: "))

        if escolha == 1:
            self.adicionar()
       
        elif escolha == 2:
            self.alterar2()
            
        elif escolha == 3:
            self.pesquisar()

        elif escolha == 4:
            self.remover()
        
        elif escolha == 5:
            self.all()
        
        elif escolha == 6:
            self.final()

        elif escolha != 1 or escolha != 2 or escolha != 3 or escolha != 4 or escolha != 5 or escolha != 6:
            self.adicionar()
            
            
        else:
            print("\nerro!")

    
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

        print("\n1- voltar ao menu")
        print("\n2- fim do programa")
        escolha2 = int(input("\nO que deseja fazer? "))
        if escolha2 == 1:
            self.menu()
        elif escolha2 == 2:
            self.final()
        else:
            print("\nerro")
        
    def alterar2(self):
        print(self.lista)
        palavra = str(input("\nqual dado deseja alterar? "))
        if palavra in self.lista:
            posicao = self.lista.index(palavra)
            modificacao = str(input("\nColoque a modificação: "))
            self.lista[posicao] = modificacao
        else: 
            print("\nNão está na lista!")
        print(self.lista)
        
        print("\n1- voltar ao menu")
        print("\n2- fim do programa")
        escolha2 = int(input("\nO que deseja fazer? "))
        if escolha2 == 1:
            self.menu()
        elif escolha2 == 2:
            self.final()
        else:
            print("\nerro")

    def pesquisar(self):
        print(self.lista)
        print("\n1- voltar ao menu")
        print("\n2- fim do programa")
        escolha2 = int(input("\nO que deseja fazer? "))
        if escolha2 == 1:
            self.menu()
        elif escolha2 == 2:
            self.final()
        else:
            print("\nerro")

    def remover(self):
        posicao = int(input('\nqual posição vai remover: '))
        del (self.lista[posicao])
        print(self.lista)
        
        print("\n1- voltar ao menu")
        print("\n2- fim do programa")
        escolha2 = int(input("\nO que deseja fazer? "))
        if escolha2 == 1:
            self.menu()
        elif escolha2 == 2:
            self.final()
        else:
            print("\nerro")

    def final(self):
        print("\n\nObrigado por usar nosso APP\n\n")
    
    def all(self):
        print("\nTem certeza que quer deletar tudo? ")
        print("\n1 - pra sim")
        print("\n2 - para não")
        num2 = int(input("\nqual sua escolha: "))
        if num2 == 1:
            print(self.lista)
            print("\nDados deletados")
            del (self.lista)
            print("\n>>>>>>Lista vazia<<<<<<<")
            print("\n1- voltar ao menu")
            print("\n2- fim do programa")
            escolha2 = int(input("\nO que deseja fazer:  "))
            if escolha2 == 1:
                    self.menu()
            elif escolha2 == 2:
                    self.final()
            else:
                    print("\nerro")
            
        elif num2 == 2:
                print("\n1- voltar ao menu")
                print("\n2- fim do programa")
                escolha2 = int(input("\nO que deseja fazer:  "))
                if escolha2 == 1:
                    self.menu()
                elif escolha2 == 2:
                    self.final()
                else:
                    print("\nerro")
        else: 
            print("\nerro!")
            

        
        
lista = []
object = Cruds(lista)
object.menu()
object.adicionar()
object.alterar2()
object.pesquisar()
object.remover()
object.final()
object.all()