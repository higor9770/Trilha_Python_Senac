# Fazer um programa que através de uma função Principal(), receba o
# salário atual de um funcionário, calcule o valor do novo salário,
# reajustado de acordo com a tabela abaixo: Deve ter uma função para
# cada reajuste.

def principal(salario):

    if salario <= 500:
        nov_sal = salario*0.15
        print("sua gratificacao é de 15% e voce ganhou:", nov_sal, " a mais no seu salario")
    elif salario > 500 and salario <1000:
        nov_sal = salario*0.10
        print("sua gratificacao é de 10% e voce ganhou:", nov_sal, " a mais no seu salario")
    elif salario > 1000:
        nov_sal = salario*0.05
        print("sua gratificacao é de 5% e voce ganhou:", nov_sal, " a mais no seu salario")

salario = int(input("digite seu salario: "))
principal(salario)