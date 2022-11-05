# Faça um programa que receba do usuário o nome do aluno e sua
# matricula. Retorne essas informações na tela. Em seguida, pergunte ao
# usuário se ele vai querer alterar algum dado de seu cadastro, em
# seguida você deverá realizar essa operação de alteração. Como fará
# isso? Através de funções. A primeira função será alterarNome(nome) e a
# segunda função será alterarMatricula(matricula). Retorne na tela o dado
# que foi alterado. Dica: Use condicionais.

def alterarNome(nome):
    
    alterar = nome
    return alterar

def alterarMatricula(matricula):
    
    alterarMat = matricula
    return alterarMat

def menu():


    nome = input("digite seu nome: ")
    matricula = int(input("digite sua matricula: "))


    print("bem vindo ao menu")
    print("----------------------------------------")
    print(">> digite 1 para ver seu perfil")
    print(">> digite 2 para alterar seu nome")
    print(">> digite 3 para alterar seu matricula")
    print("----------------------------------------")

    escolha = int(input("qual sua escolha? "))


    if escolha == 1:
        print("seus dados: ", nome, matricula)
    elif escolha == 2:
        print("<<<<<<<< vamos alterar os dados >>>>>>>>>")
        nome = input("digite seu novo nome: ")
        print("<<<<<<<>>>>>>>><<<<<<<>>>>>>>><<<<<>>>>>>")
        print("dado alterado!")
        print("seu novo nome é: ", alterarNome(nome))
    elif escolha == 3:
        print("<<<<<<<< vamos alterar os dados >>>>>>>>>")
        matricula = input("digite seu novo nome: ")
        print("<<<<<<<>>>>>>>><<<<<<<>>>>>>>><<<<<>>>>>>")
        print("dado alterado!")
        print("a sua nova matricula é: ", alterarMatricula(matricula))
    else:
        print("erro!")



menu()