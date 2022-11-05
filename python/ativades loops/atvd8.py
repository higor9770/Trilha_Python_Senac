nome = str(input("digite um nome com menos de 3 caracteres: "))
while len(nome) <=3:
    nome = str(input("digite um nome com menos ou igual a 3 caracteres: "))
idade = int(input("digite sua idade: "))
while idade < 0 or idade >150:
    print("idade inválida")
    idade = int(input("'digite sua idade novamente"))
salario = float(input("digite seu salário"))
while salario <0:
    salario = float(input("salário errado! Digite um valor salárial maior que zero"))
