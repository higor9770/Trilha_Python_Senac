# Crie um jogo em Python onde o computador vai sortear um número
# entre 1 até 10. Deve criar uma função para retornar esse número
# aleatório. Em seguida, crie uma função principal que irá chamar a outra
# função e guardar esse número gerado. Em seguida, você vai tentar
# adivinhar que número foi esse. A cada tentativa, ele vai te dizer se seu
# palpite foi alto, baixo ou se você acertou.

#  Irá precisar importar a biblioteca, random;
#  O número gerado deve estar entre 1 e 10;
#  Guarde o número gerado dentro de uma variável;
#  Pode utilizar laços de repetição e condicionais.
#  Irá utilizar a função randint;

import random



def numAleatorio ():

    return random.randint(1,50)

def principal():

    numale = numAleatorio()
    teste = 0

    while teste != numale:
        teste = int(input("\n tente acertar o número: "))
        if teste < numale:
            print("\n O número é menor que o número aleatório digitado.")
        elif teste > numale:
            print("\n O número é maior que o número aleatório digitado.")
        elif teste == numale:
            print("\n acertou!!!")
        else:
            print("\n erro!")
principal()

