# Faça um programa que leia um nome de usuário e a sua senha. Não
# aceite a senha igual ao nome do usuário, caso isso ocorra, deve mostrar
# uma mensagem de erro e voltar a pedir as informações.

nome =  str(input("digite seu nome: "))
senha = str(input("digite sua senha: "))

while nome == senha:
    print("o nome é igual a senha")
    senha = str(input("digite sua senha novamente: "))

print("nota valida")