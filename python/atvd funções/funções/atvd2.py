# Faça um programa que contenha 3 funções: A primeira é uma função de
# soma de três números, a segunda é uma função de média que irá
# receber a função soma para calcular a média. E a terceira função será
# uma função de menu para receber os números dos usuários.

def soma(num1 , num2, num3):
    somas = num1 + num2 + num3
    return somas


def media(soma):
     
    medias = soma/3
    return medias

def menu():
    num1 = int(input("digite o primeiro número: "))
    num2 = int(input("digite o segundo número: "))
    num3 = int(input("digite o terceiro número: "))

    print("a soma é: ",soma(num1, num2, num3))
    print("a media é: ",media(soma(num1, num2, num3)))
    

menu()