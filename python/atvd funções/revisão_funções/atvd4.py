# Faça uma função chamada soma que irá receber dois parâmetros (n1,
# n2) em seguida deverá fazer o calculo da soma . De maneira similar,
# faça outra função chamada de subtracao, também irá receber dois
# parâmetros (n1, n2) e calcular a diferença. Agora que temos as duas
# funções, iremos criar a função principal() ela ficará responsável por
# receber a função soma e a função subtração, e claro os valores
# repassados pelos os usuários. Imprimam na tela os resultados.

def somas(n1, n2):

    soma = n1 + n2
    return soma

def subtracao(n1, n2):

    sub = n1 - n2
    return sub

def principal():

    n1 = int(input("digite o primeiro numero: "))
    n2 = int(input("digite o segundo numero: "))

    cal = int(input("\n deseja calcula a soma ou a subtracao? \n\n 1- soma \n 2- subtracao \n\n digite a sua escolha: "))

    if cal == 1:
       print("\n",somas(n1, n2))
    elif cal == 2:
       print("\n",subtracao(n1,n2))
    else:
        print("erro!")

principal()
