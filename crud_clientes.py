import mysql.connector  # Importa o conector do MySQL para Python

class Database:
    def __init__(self):
        # Construtor da classe, chamado automaticamente ao criar uma instância da classe Database
        try:
            self.connection = mysql.connector.connect(
                host="localhost",        # Endereço do servidor do banco
                user="root",             # Usuário do banco de dados
                password="",             # Senha do banco de dados
                database="farmacia_sa"   # Nome do banco de dados
            )
            self.cursor = self.connection.cursor()  # Cria um cursor para executar comandos SQL
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def inserir_cliente(self, nome, senha, email, telefone, cpf):
        # Insere um novo cliente com todos os campos
        try:
            query = """
                INSERT INTO cliente (nome, senha, email, telefone, cpf)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (nome, senha, email, telefone, cpf))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao inserir cliente: {e}")

    def alterar_cliente(self, idcliente, nome, senha, email, telefone, cpf):
        # Atualiza os dados de um cliente com base no ID
        try:
            query = """
                UPDATE cliente
                SET nome = %s, senha = %s, email = %s, telefone = %s, cpf = %s
                WHERE idcliente = %s
            """
            self.cursor.execute(query, (nome, senha, email, telefone, cpf, idcliente))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao alterar cliente: {e}")

    def excluir_cliente(self, idcliente):
        # Exclui um cliente com base no ID
        try:
            query = "DELETE FROM cliente WHERE idcliente = %s"
            self.cursor.execute(query, (idcliente,))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao excluir cliente: {e}")

    def listar_clientes(self):
        # Retorna todos os clientes cadastrados
        try:
            query = "SELECT * FROM cliente"
            self.cursor.execute(query)
            return self.cursor.fetchall()  # Retorna uma lista de tuplas com os dados
        except mysql.connector.Error as e:
            print(f"Erro ao listar clientes: {e}")
            return []

    def fechar_conexao(self):
        # Fecha a conexão com o banco de dados
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
