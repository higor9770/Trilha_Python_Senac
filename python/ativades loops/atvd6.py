# Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja diferente do intervalo pedido. E continue
# pedindo até que o usuário informe um valor válido. Use a estrutura de
# repetição while.

nota = int(input("digite um número entre 0 e 10: "))

print("------------------------ checkando a nota --------------------------")

if nota >= 0 and nota <=10:
    print("nota válida")
else:
    while nota < 0 or nota > 10:
         input("erro!")
         nota = int(input("digite a nota nota novamento: "))