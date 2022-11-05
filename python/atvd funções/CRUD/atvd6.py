# Crie uma classe Petshop que ira receber um construtor inicializado com
# apenas um argumento. No petshop tem as seguintes características:
#  Venda de ração, banho/tosa, Médico veterinário;
#  Essas três características deverão ser transformadas em
# métodos;
#  Deverá perguntar ao usuário qual opção acima irá escolher;
#  Se ele escolher venda, dentro do método deverá ter 3 opções de
# rações: Premium, Pro, Basic. Retorne de acordo com a escolha
# do usuário.
#  Se ele escolher banho/tosa deverá mostrar ao usuário o dia
# disponível e o preço do serviço, como mostra a seguir:
# print(‘Banho e tosa = Dia 06 - Preço = 100’)

#  Agora se ele escolher médico, deverá mostrar quais médicos
# estão disponíveis e mandar ele agendar com o medico da sua
# escolha. E imprima o que o usuário escolheu. Nesse Petshop só
# tem dois médicos, um pela manhã e outro a noite.

class petshop:

    def __init__(self):
        pass


    def VendaDeRancao(self):

        print("opções de rações")
        print("1- Premium")
        print("2- Pro")
        print("3- Basic")

        racao = int(input("Digite a racao que deseja comprar: "))
        if racao == 1:
            print("Premium")
        elif racao == 2:
            print("Pro")
        elif racao == 3:
            print("Basic")
        else:
            print("erro!")
    def banhoTosa(self):

        print("1- Banho e tosa = Dia 06 - Preço = 100 ")
        print("2- Banho e tosa = Dia 07 - Preço = 100 ")
        print("3- Banho e tosa = Dia 08 - Preço = 100 ")
        print("\n obs: outro dia: sem vaga")


        self.escolha = int(input("escolha qual dia deseja marcar que deseja comprar: "))
        if self.escolha == 1:
            print("Marcado! Compareça no dia 06")

        elif self.escolha == 2:
            print("Marcado! Compareça no dia 07")
        elif self.escolha == 3:
            print("Marcado! Compareça no dia 08")
        else:
            print("sem data!")
        

    def medicoVet(self):

        agend = int(input("Qual horario você quer escolher? 1- noite / 2- manhã"))

        if agend == 1:
            print("temos duas opções de horários para noite")
            print("1- 18:00")
            print("2- 19:00")
        elif agend == 2:
            print("temos duas opções de horários para manhã")
            print("1- 10:00")
            print("2- 09:00")
        else:
            print("erro")


        

object = petshop()
object.VendaDeRancao()
object.banhoTosa()
object.medicoVet()
