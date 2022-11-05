# Faça duas funções dobro(), metade(). Peça ao usuário um valor que ele
# tem na carteira, se ele tiver acima de 50 reais deverá retirar a metade do
# dinheiro, se ele tiver abaixo de 50, deverá dobrar o dinheiro dele.


def dobro(carteira):
    if carteira < 50:
        valor = carteira * 2
        print("você ganhou o dobro: ", valor)



def metade(carteira):
    if carteira > 50:
        valor = carteira/2
        print("você perdeu metade do valor: ", valor)


carteira = float(input("digite o valor que possui na sua carteira: "))
