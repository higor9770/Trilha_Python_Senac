from ContatoDAO import *

def main():
    while (True):
        print('..PythonDB Opções..')
        print('1 -> Adicionar')
        print('2 -> pesquisar')
        print('3 -> Alterar')
        print('4 -> Deletar')
        print('0 -> Encerrar')
        opcao = int(input('Opção..: '))

        print()

        if opcao == 0:
            encerrar()
        elif opcao == 1:
            adicionar()
        elif opcao == 2:
            pesquisar()
        elif opcao == 3:
            alterar()
        else:
            print('Opção Incorreta.')
            print()

def encerrar():
    print('Encerrado.')
    exit(0)

def adicionar():
    print("1- tabela professor")
    print("2- tabela coordenador")
    print("3- tabela sala")
    escolha = int(input("digite o número do que você quer adicionar:"))
    if escolha == 1:
        print('------------- [PROFESSOR] -------------')
        try:
            professor = Professor()
            professor.setcpf(input('CPF: '))
            professor.setnome(input('Nome: '))
            professor.settelefone(input('Telefone: '))
            professor.setemail(input('Email: '))
            professor.setdata_nascimento(input('data nascimento: '))
            professor.setsexo(input('Sexo: '))
            cdao.add1(professor)
        except Exception as e:
            print(e)
        print('----------------------------------------')
    elif escolha ==2:
        print('------------- [COORDENADOR] -------------')
        try:
            coordenador = Coordenador()
            coordenador.setcpf(input('CPF: '))
            coordenador.setnome(input('Nome: '))
            coordenador.settelefone(input('Telefone: '))
            coordenador.setemail(input('Email: '))
            coordenador.setdata_nascimento(input('data nascimento: '))
            coordenador.setsexo(input('Sexo: '))
            cdao.add2(coordenador)
        except Exception as e:
            print(e)
        print('----------------------------------------')
    elif escolha ==3:
        print('------------- [SALA DE AUla] -------------')
        try:
            contato = Professor()
            contato.setcpf(input('CPF: '))
            contato.setnome(input('Nome: '))
            contato.settelefone(input('Telefone: '))
            contato.setemail(input('Email: '))
            contato.setdata_nascimento(input('data nascimento: '))
            contato.setsexo(input('Sexo: '))
            cdao.add3(contato)
        except Exception as e:
            print(e)
        print('----------------------------------------')
    else:
        print("erro!")

def pesquisar():
    print('----------- [BUSCAR (TODOS)] -----------')
    try:
        professor = cdao.getprofessor()
        if professor is not None:
            for professor in professor:
                print('Contato: (ID: {}) {} | {} | {}'.format(professor.getcpf(), professor.getnome(), professor.gettelefone(), professor.getemail()))
    except Exception as e:
        print(e)
    print('----------------------------------------')

def alterar():
    print('-------------- [ALTERAR] --------------')
    try:
        professor = Professor()
        professor.setcpf(lerint('CPF: '))
        professor.setnome(input('Novo nome: '))
        professor.settelefone(input('Novo telefone: '))
        professor.setemail(input('Novo email: '))
        cdao.update(professor)
    except Exception as e:
        print(e)
    print('----------------------------------------')

""" def deletar():
    print('-------------- [DELETAR] --------------')
    try:
        cdao.delete(lerint('ID: '))
    except Exception as e:
        print(e)
    print('----------------------------------------') """

def lerint(mensagem):
    try:
        i = int(input(mensagem))
    except:
        i = -1
    return i


cdao = ContatoDAO()
main()
