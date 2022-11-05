lista=[]


num1 = int(input('número: '))
lista.append(num1)
num2 = int(input('número: '))
lista.append(num2)
num3 = int(input('número: '))
lista.append(num3) 

print('lisat crescente: ', lista)
lista.sort()

lista.sort(reverse = True)
print('lisat decrescente: ', lista)

