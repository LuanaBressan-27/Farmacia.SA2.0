import mysql.connector  # Importa o conector do MySQL para Python

class Database:
    def __init__(self):
        # Construtor da classe, chamado automaticamente ao criar uma instância da classe Database
        try:
            # Estabelece a conexão com o banco de dados MySQL
            self.connection = mysql.connector.connect(
                host="localhost",     # Endereço do servidor do banco (neste caso, local)
                user="root",          # Nome de usuário do banco de dados
                password="",          # Senha do banco de dados (vazia neste caso)
                database="farmacia_sa" # Nome do banco de dados que será utilizado
            )
            self.cursor = self.connection.cursor()  # Cria um cursor para executar comandos SQL
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")  # Exibe erro caso a conexão falhe

    def inserir_cliente(self, nome, senha):
        # Insere um novo cliente na tabela 'cliente'
        try:
            query = "INSERT INTO cliente (nome, senha) VALUES (%s, %s)"  # Comando SQL com parâmetros
            self.cursor.execute(query, (nome, senha))  # Executa a query com os valores fornecidos
            self.connection.commit()  # Confirma as alterações no banco de dados
        except mysql.connector.Error as e:
            print(f"Erro ao inserir cliente: {e}")  # Exibe erro em caso de falha

    def alterar_cliente(self, idcliente, nome, senha):
        # Atualiza os dados de um cliente existente com base no ID
        try:
            query = "UPDATE cliente SET nome = %s, senha = %s WHERE idcliente = %s"
            self.cursor.execute(query, (nome, senha, idcliente))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao alterar cliente: {e}")

    def excluir_cliente(self, idcliente):
        # Remove um cliente da tabela com base no ID
        try:
            query = "DELETE FROM cliente WHERE idcliente = %s"
            self.cursor.execute(query, (idcliente,))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao excluir cliente: {e}")

    def listar_clientes(self):
        # Retorna todos os clientes cadastrados na tabela
        try:
            query = "SELECT * FROM cliente"
            self.cursor.execute(query)
            return self.cursor.fetchall()  # Retorna os resultados como uma lista de tuplas
        except mysql.connector.Error as e:
            print(f"Erro ao listar clientes: {e}")
            return []  # Retorna lista vazia em caso de erro

    def fechar_conexao(self):
        # Fecha o cursor e a conexão com o banco de dados
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
