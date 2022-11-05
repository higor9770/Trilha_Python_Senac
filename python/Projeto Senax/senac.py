import mysql.connector 

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'teste',
    database = 'senac',
)

cursor = conexao.cursor()
""" #insert 
cpf = input("digite seu cpf: ")
nome = input('digite seu nome: ')
telefone = int(input('digite seu telefone: '))
email = input('digite seu email: ')
data_nascimento = input("digite sua data de nascimento (data, mês, ano): ")
sexo = input('digite seu sexo (FE, MA, NB): ')

comando = f'INSERT INTO professor (CPF, NOME, TELEFONE, EMAIL, DATA_NASCIMENTO, SEXO) VALUES ("{cpf}", "{nome}", {telefone}, "{email}", "{data_nascimento}", "{sexo}") '
cursor.execute(comando)
conexao.commit()
# resultado = cursor.fetchall()
cursor.close()
conexao.close() 
 """

# READ
print("1- tabela professor")
print("2- tabela coordenador")
print("3- tabela sala")
ver = input("digite o número da tabela que você quer visualizar os dados:")
if ver == 1:
    comando = f'SELECT * FROM professor'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler o banco de dados
    print("essa é minha tabela professor: \n", resultado,"\n")
elif ver == 2:
    comando = f'SELECT * FROM coordenador'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler o banco de dados
    print("essa é minha tabela coordenador: \n", resultado,"\n")
elif ver == 3:
    comando = f'SELECT * FROM sala'
    cursor.execute(comando)
    resultado = cursor.fetchall() # ler o banco de dados
    print("essa é minha tabela sala de aula: \n", resultado,"\n")