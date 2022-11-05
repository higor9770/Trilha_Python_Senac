listaSet= set()
for recebe in range(5):
    nome = str(input("Seu nome: "))
    estado = str(input("estado: "))
    listaSet.add(nome)
    listaSet.add(estado)

print(listaSet)
print(type(listaSet))