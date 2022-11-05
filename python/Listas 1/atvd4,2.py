
lista = []
contador = 1
while contador <= 5:
    numero = float(input('número: '))
    lista.append(numero)
    contador = contador + 1
    lista.sort()
print(lista)
lista.sort(reverse =True)
print(lista)
