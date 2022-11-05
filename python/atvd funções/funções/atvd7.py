# Jogo da sorte: Crie um módulo chamado de roleta.py que tenha a função
# incorporada: premiado(valor). Dentro da função terá dois

# randint, começando com intervalo 0 e terminando com valor do dinheiro
# digitado.O primeiro randint, irá retornar o número aleatório e somar com
# o dinheiro que o usuário digitou. O segundo irá subtrair o numero
# aleatório com o valor da soma. Deverá mostrar na tela os números
# aleatórios que saíram e o total que ele ganhou jogando a roleta da sorte.
# Modelo exemplo:

import random

def premiado(dinheiro):


    sorte = random.randint(0, dinheiro)

    soma = sorte + dinheiro
    print("o número da sorte: ", sorte)
    print("você ganhou: ", soma)

    azar = random.randint(0, dinheiro)
    sub = soma - sorte
    print("o número de azar foi: ",azar)
    print("você perdeu: ",sub)


dinheiro = int(input("qual o valor: "))
premiado(dinheiro)
