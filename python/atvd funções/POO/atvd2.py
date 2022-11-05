class bola:
    def __init__(self, tamanho, cor,  circunferencia, raio, marca):
        self.cor = cor
        self.marca = marca
        self.tamanho = tamanho
        self.circunferencia = circunferencia
        self.raio = raio
        print("A cor: ", self.cor)
        print("A marca: ", self.marca)
        print("O tamanho: ", self.tamanho)
        print("A circunferencia: ", self.circunferencia)
        print("O raio é: ", self.raio)

    def mudarCor(self, cor):
        self.cor = cor
        print("\nvamos mudar de cor >>>\n")
        self.cor = input("\nDigite uma nova cor para essa bola: \n")
        print("os novos dados são: ")
        print("marca: ", marca)
        print("tamanho: ", tamanho)
        print("A nova cor: ",self.cor)
        print("circunferencia: ",circunferencia)
        print("raio: ", raio)


cor = input("digite a cor: ")
marca = input("digite a marca: ")
tamanho = input("digite o tamanho: ")
circunferencia = int(input("digite a circunferencia da bola: "))
raio = int(input("digite o raio da bola: "))
object = bola(tamanho, cor, circunferencia, raio, marca)
object.mudarCor(cor)