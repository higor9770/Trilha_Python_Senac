# Faça uma função que irá receber dados dos usuários como: nome,
# idade e estado civil. Caso o usuário não informe os parâmetros deverá
# fazer parâmetros padrões para resolver isso. Deverá retornar da
# seguinte forma: nome:não informado, idade = 0, estado civil = não
# informado.

def dados(nome = "nao informado", idade = 0 , estcivil = "nao informado"):

   
    print(nome)
    print(idade)
    print(estcivil)


nome = str(input("digite o nome: "))
idade = int(input("digite a idade: "))
estcivil = str(input("digite o estado civil: "))


dados(nome, idade)