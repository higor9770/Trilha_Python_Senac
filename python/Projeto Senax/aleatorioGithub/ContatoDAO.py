from ConnectionFactory import *
from Contato import *

class ContatoDAO:
    def __init__(self):
        self.__cf = ConnectionFactory()
        

    def add1(self, professor):
        try:
            con = self.__cf.getconnection()
            
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("INSERT INTO contato(cpf, nome, telefone, email, data_nasciemnto, sexo) VALUES(%s, %s, %s)", (professor.getcpf(), professor.getnome(), professor.gettelefone(), professor.getemail(), professor.getdata_nasciemnto(), professor.getsexo()))
                con.commit()
                if cursor.rowcount > 0:
                    print('Contato adicionado.')
                else:
                    print('Contato não adicionado.')
        except:
            print('Não foi possível adicionar o contato.')
            con.rollback()
        finally:
            self.__cf.closeconnection(con)
    
    def add2(self, coordenador):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("INSERT INTO contato(cpf, nome, telefone, email, data_nasciemnto, sexo) VALUES(%s, %s, %s)", (coordenador.getcpf(), coordenador.getnome(), coordenador.gettelefone(), coordenador.getemail(), coordenador.getdata_nasciemnto(), coordenador.getsexo()))
                con.commit()
                if cursor.rowcount > 0:
                    print('Contato adicionado.')
                else:
                    print('Contato não adicionado.')
        except:
            print('Não foi possível adicionar o contato.')
            con.rollback()
        finally:
            self.__cf.closeconnection(con)

    def add3(self, sala):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("INSERT INTO contato(cpf, nome, telefone, email, data_nasciemnto, sexo) VALUES(%s, %s, %s)", (sala.getcpf(), sala.getnome(), sala.gettelefone(), sala.getemail(), sala.getdata_nasciemnto(), sala.getsexo()))
                con.commit()
                if cursor.rowcount > 0:
                    print('Contato adicionado.')
                else:
                    print('Contato não adicionado.')
        except:
            print('Não foi possível adicionar o contato.')
            con.rollback()
        finally:
            self.__cf.closeconnection(con)

    def getprofessor(self):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("SELECT * FROM professor")
                result = cursor.fetchall()
                length = len(result)
                if len(result) > 0:
                    contatos = []
                    for i in range(length):
                        contatos.append(Professor(result[i][0], result[i][1], result[i][2], result[i][3]))
                    return contatos;
                else:
                    print('Não existem contatos.')
        except:
            print('Não foi possível buscar os contatos.')
        finally:
            self.__cf.closeconnection(con)
        
    def getcoordenador(self):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("SELECT * FROM coordenador")
                result = cursor.fetchall()
                length = len(result)
                if len(result) > 0:
                    contatos = []
                    for i in range(length):
                        contatos.append(Coordenador(result[i][0], result[i][1], result[i][2], result[i][3]))
                    return contatos;
                else:
                    print('Não existem contatos.')
        except:
            print('Não foi possível buscar os contatos.')
        finally:
            self.__cf.closeconnection(con)
    
    def getsala(self):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("SELECT * FROM sala")
                result = cursor.fetchall()
                length = len(result)
                if len(result) > 0:
                    contatos = []
                    for i in range(length):
                        contatos.append(Sala(result[i][0], result[i][1], result[i][2], result[i][3]))
                    return contatos;
                else:
                    print('Não existem contatos.')
        except:
            print('Não foi possível buscar os contatos.')
        finally:
            self.__cf.closeconnection(con)

    def update(self, professor):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("UPDATE contato SET nome = %s, telefone = %s, email = %s WHERE id = %s", (professor.getcpf(), professor.getnome(), professor.gettelefone(), professor.getemail(), professor.getdata_nascimento(), professor.getsexo()))
                con.commit()
                if cursor.rowcount > 0:
                    print('Contato alterado com sucesso.')
                else:
                    print('Não existe contato com esse ID.')
        except:
            print('Não foi possível alterar/atualizar o contato.')
        finally:
            self.__cf.closeconnection(con)
    
    def update(self, coordenador):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("UPDATE contato SET nome = %s, telefone = %s, email = %s WHERE id = %s", (coordenador.getcpf(), coordenador.getnome(), coordenador.gettelefone(), coordenador.getemail(), coordenador.getdata_nascimento(), coordenador.getsexo()))
                con.commit()
                if cursor.rowcount > 0:
                    print('Contato alterado com sucesso.')
                else:
                    print('Não existe contato com esse ID.')
        except:
            print('Não foi possível alterar/atualizar o contato.')
        finally:
            self.__cf.closeconnection(con)

    def update(self, sala):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("UPDATE contato SET nome = %s, telefone = %s, email = %s WHERE id = %s", (sala.getcpf(), sala.getnome(), sala.gettelefone(), sala.getemail(), sala.getdata_nascimento(), sala.getsexo()))
                con.commit()
                if cursor.rowcount > 0:
                    print('Contato alterado com sucesso.')
                else:
                    print('Não existe contato com esse ID.')
        except:
            print('Não foi possível alterar/atualizar o contato.')
        finally:
            self.__cf.closeconnection(con)


    def delete(self):
        try:
            con = self.__cf.getconnection()
            if con.is_connected():
                cursor = con.cursor()
                cursor.execute("DELETE FROM TABLE Professor" , (Professor,))
                con.commit()
                if cursor.rowcount > 0:
                    print('Tabela deletada com sucesso.')
                else:
                    print('Não existe tabla com esse ID.')
        except:
            print('Não foi possível excluir/remover o contato.')
        finally:
            self.__cf.closeconnection(con)
