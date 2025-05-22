import mysql.connector
from mysql.connector import Error  # Importa exceções específicas para manipular erros do MySQL

class Database:
    def __init__(self):
        # Parâmetros para conexão com o banco MySQL
        self.MYSQL_HOST = "localhost"          # Host do servidor MySQL (local)
        self.MYSQL_USER = "root"               # Usuário do banco
        self.MYSQL_PASSWORD = ""               # Senha do usuário (aqui está vazia)
        self.MYSQL_DATABASE = "farmacia_sa"   # Nome do banco de dados que será usado/criado

        # Ao criar a instância da classe, já garantimos que o banco e a tabela existam
        self.initialize_database()

    def connect(self):
        """
        Método para abrir conexão com o banco de dados.
        Ele configura o objeto 'conn' que representa a conexão, e 'cursor' para executar comandos SQL.
        """
        try:
            self.conn = mysql.connector.connect(
                host=self.MYSQL_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD,
                database=self.MYSQL_DATABASE  # Define o banco a ser usado nesta conexão
            )
            self.cursor = self.conn.cursor()  # Cursor para enviar comandos SQL ao banco
        except Error as e:
            # Caso algo dê errado na conexão, imprime o erro e repassa a exceção
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def disconnect(self):
        """
        Método para fechar o cursor e a conexão.
        Importante para evitar vazamentos de memória e conexões abertas no servidor.
        """
        if self.cursor:
            self.cursor.close()  # Fecha o cursor que executa queries
        if self.conn:
            self.conn.close()    # Fecha a conexão com o banco de dados

    def initialize_database(self):
        """
        Método que cria o banco de dados e a tabela 'adm' caso não existam.
        Usa uma conexão sem banco selecionado inicialmente, para permitir criar o banco.
        """
        try:
            # Estabelece conexão com o servidor MySQL sem escolher um banco específico
            connection = mysql.connector.connect(
                host=self.MYSQL_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD
            )
            cursor = connection.cursor()

            # Cria o banco de dados com o nome definido, caso não exista ainda
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.MYSQL_DATABASE}")

            # Seleciona o banco recém-criado ou que já existia para operações futuras
            connection.database = self.MYSQL_DATABASE

            # Cria a tabela 'adm' com colunas:
            # - idADM: chave primária auto-incrementada
            # - nome: nome do administrador, campo obrigatório
            # - senha: senha do administrador, campo obrigatório
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS adm (
                    idADM INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    senha VARCHAR(50) NOT NULL
                )
            """)

            # Aplica as mudanças feitas (criação do banco e tabela) no servidor MySQL
            connection.commit()

        except Error as e:
            # Caso ocorra algum erro durante a criação do banco ou tabela, imprime para debug
            print(f"Erro ao inicializar o banco de dados: {e}")

        finally:
            # Certifica-se de fechar cursor e conexão, mesmo em caso de erro,
            # para liberar recursos do sistema e não deixar conexões abertas
            if cursor:
                cursor.close()
            if connection:
                connection.close()
