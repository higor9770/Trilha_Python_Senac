def numeros( num1, num2):

    if num1 < num2:
        print("o número dois é maior que o primeiro")
    elif num1 > num2:
        print("o número um é maior que o segundo")
    else: 
        print("os números são iguais")
    
num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))

numeros(num1, num2)