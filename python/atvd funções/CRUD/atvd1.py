class funcionario: 

    def __init__(self, nome, salario):
        self.salario = salario
        self.nome = nome

    def mostrarNome(self):
        print(self.nome)
    
    def mostrarSalario(self):
        print(self.salario)

