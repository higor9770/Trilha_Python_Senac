import mysql.connector


class ConnectionFactory:
    def getconnection(self):
        try:    
                con = mysql.connector.connect(
                host="localhost",
                port="3306",
                user="root",
                passwd="teste",
                database="senac"
            )
        except:
            print('Não foi possível realizar a conexão.')

    def closeconnection(self, con):
        con.close
