#Defina uma função chamada velocidade_media() que recebe dois
#parâmetros: a distância percorrida e o tempo gasto. Após isso, calcule a
#velocidade média. Deve existir um função menu() para receber os dados
#do usuário.


def velocidade_media(distancia, tempo):
    cal = distancia/tempo
    print("velocidade média é: ", cal)

def menu():
    distancia = float(input("digite a distancia em metros: "))
    tempo = float(input("digite o tempo em segundos: "))

    velocidade_media(distancia, tempo)

menu()