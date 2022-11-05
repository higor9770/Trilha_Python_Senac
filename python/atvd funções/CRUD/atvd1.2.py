from atvd1 import funcionario

nome = input("digite seu nome: ")
salario = int(input("digite seu salario: "))

object = funcionario(nome, salario)
object.mostrarSalario()
object.mostrarNome()