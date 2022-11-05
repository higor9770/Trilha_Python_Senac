""" Crie uma classe que modele um aluno. Atributos dentro do construtor:
nome, numero de matrícula e curso. Métodos: mostrar curso e alterar
curso. A chamada do objeto deverá ser em outro arquivo
Modelo desejado: """
class aluno: 

    def __init__(self):
       
        nome = str(input("digite seu nome: "))
        matricula = int(input("digite sua matricula: "))
        curso = input("digite seu curso: ")
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrarCurso(self):
        print(self.nome)
        print(self.curso)
        print(self.matricula)

    def alterarCurso(self):
        curso = (input('Qual o nome do novo curso: '))
        self.curso = curso
        print(self.curso)

