#4. Crie um programa que tenha uma função chamada voto() que vai
#receber como parâmetro o ano atual e o ano de nascimento de uma
#pessoa, retornando a informação se a pessoa tem o voto
#negado,opcional ou obrigatório nas eleições. Seguindo o pressuposto
#que: menor que 16 anos, não vota. Maior ou igual a 16 e menor de 18 é
#opcional e também maior que 65 anos, também será opcional. O
#restante das idades será obrigatório.


def voto(ano, nascimento):
    
    valor = nascimento - ano
    print(valor)
   
    if valor >= 18:
        print("obrigatório")
    elif valor >= 16 or valor > 65:
            print("opcional")
    elif valor < 16:
            print("negado")
    else:
            (print("erro"))

ano = int(input("informe o ano atual: "))
nascimento = int(input("ano de nascimento: "))
voto(ano, nascimento)