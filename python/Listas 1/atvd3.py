#Faça um programa que leia 2 números pelo teclado e guarde em uma
#lista.No final mostre quem é o maior e o menor da lista. Lembre-se que
#tem que fazer a conversão do inteiro. '''

lista = [] # lista não inicializada para recebe do usuários 
numero1 = int(input('digite um número: '))
lista.append(numero1)
numero2 = int(input('digite um número: '))
lista.append(numero2)

print(lista)

if lista[0]>lista[1]:
     print('o menor núumero é:  ', lista[1])
    
else:
     print('o maior número é:  ', lista[1])