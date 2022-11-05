import mysql.connector 

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'teste',
    database = 'senac',
)

cursor = conexao.cursor()


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

# READ
""" comando = f'SELECT * FROM professor'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

cursor.close()
conexao.close() """


























    
""" def inserir(self, conexao):

            nome = input('Diga o nome: ')
            telefone = input('Informe o telefone: ')
            email = input('Informe seu email: ')
            vsql = "INSERT INTO tb_contatos (T_NOME, T_TELEFONE, T_EMAIL) VALUES ('" + nome + "','" + telefone + "','" + email + "')"

            c = conexao.cursor()
            c.execute(vsql)
            conexao.commit()
            print('Inserido com sucesso!')


    def remover(self, conexao):

            vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO =1"

            c = conexao.cursor()
            c.execute(vsql)
            conexao.commit()
            print('Removido com sucesso!')

    def atualizar(self, conexao):

            vsql = "UPDATE tb_contatos SET T_NOME='maria', T_TELEFONE='43444444', T_EMAIL='marialimaoliveira@gmail.com' WHERE N_IDCONTATO=2 "
            c = conexao.cursor()
            c.execute(vsql)
            conexao.commit()
            print('Alterado com sucesso!')

    def consulta(self, conexao):

            vsql = "SELECT * FROM tb_contatos"
            c = conexao.cursor()
            c.execute(vsql)
            resultado = c.fetchall()
            return resultado
            print(resultado) """
