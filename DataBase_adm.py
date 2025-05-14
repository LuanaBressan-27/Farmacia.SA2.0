import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        # Configurações do banco de dados
        self.MYSQL_HOST = "localhost"
        self.MYSQL_USER = "root"
        self.MYSQL_PASSWORD = ""
        self.MYSQL_DATABASE = "farmacia_sa2.0"

        # Inicializa o banco de dados e cria a tabela, se não existir
        self.initialize_database()

    def connect(self):
        # Criar uma conexão com o banco de dados
        try:
            self.conn = mysql.connector.connect(
                host=self.MYSQL_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD,
                database=self.MYSQL_DATABASE
            )
            self.cursor = self.conn.cursor()
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def disconnect(self):
        # Fechar a conexão com o banco de dados
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def initialize_database(self):
        try:
            connection = mysql.connector.connect(
                host=self.MYSQL_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD
            )
            cursor = connection.cursor()
            # Criar o banco de dados, se não existir
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.MYSQL_DATABASE}")
            connection.database = self.MYSQL_DATABASE

            # Criar a tabela "adm", se não existir
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS adm (
                    idADM INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    senha VARCHAR(50) NOT NULL
                )
            """)
            connection.commit()

        except Error as e:
            print(f"Erro ao inicializar o banco de dados: {e}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
