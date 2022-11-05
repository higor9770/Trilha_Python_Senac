import calculadora


print("1. Soma\n2. Subtração\n 3. Multiplicação\n 4. Divisão")

opcao=int(input("Que operação deseja realizar: "))

n1=float(input("Primeiro numero: "))
n2=float(input("Segundo numero: "))

if opcao == 1:
    print("O resultado da soma é: ", calculadora.soma(n1,n2))

elif opcao == 2:

    print("O resultado da Subtração é:", calculadora.subtracao(n1,n2))

elif opcao == 3:

    print("O resultado da Multiplicação é:", calculadora.multiplicacao(n1,n2))

elif opcao == 4:

    print("O resultado da Divisão é:", calculadora.divisao(n1,n2))

else:

    print("opção inválida! Tente novamente")