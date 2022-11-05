class aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        
    def mostrarDados(self):
        print("os dados são: nome >", self.nome, "idade>", self.idade, "matricula>", self.matricula)

    def alterarNome(self, nome):
        self.nome = nome
        print("você quer alterar o nome?")
        print("sim - digite 1")
        print("nao - digite 2")
        cod = int(input("digite sua escolha: "))
        if cod == 1:
            self.nome = input("Digite um novo nome: ")
            print("\n o novo nome é: ", self.nome)
            print("\n sua matricula é: ", self.matricula)
            print("\n sua idade é: ", self.idade)
        elif cod == 2:
            print("obrigado por usar nosso app")
        else:
            print("erro")


nome = str(input("digite seu nome: "))
idade = int(input("digite seu idade: "))
matricula = int(input("digite seu matricula: "))
object = aluno(nome, idade, matricula)
object.mostrarDados()
object.alterarNome(nome)