import mysql.connector

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="farmacia_sa"
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def inserir_cliente(self, nome, senha):
        try:
            query = "INSERT INTO cliente (nome, senha) VALUES (%s, %s)"
            self.cursor.execute(query, (nome, senha))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao inserir cliente: {e}")

    def alterar_cliente(self, idcliente, nome, senha):
        try:
            query = "UPDATE cliente SET nome = %s, senha = %s WHERE idcliente = %s"
            self.cursor.execute(query, (nome, senha, idcliente))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao alterar cliente: {e}")

    def excluir_cliente(self, idcliente):
        try:
            query = "DELETE FROM cliente WHERE idcliente = %s"
            self.cursor.execute(query, (idcliente,))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao excluir cliente: {e}")

    def listar_clientes(self):
        try:
            query = "SELECT * FROM cliente"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Erro ao listar clientes: {e}")
            return []

    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

