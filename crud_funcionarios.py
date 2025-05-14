import mysql.connector

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="farmacia_sa2.0"
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.connection = None
            self.cursor = None

    def inserir_funcionario(self, nome, cpf, email, telefone, funcao, qtd_vendas, salario, data_inicio):
        try:
            query = """
                INSERT INTO funcionario
                (nome, cpf, email, telefone, funcao, quantidade_vendas, salario, inicio_contrato)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (nome, cpf, email, telefone, funcao, qtd_vendas, salario, data_inicio))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao inserir funcionário: {e}")

    def alterar_funcionario(self, idfuncionario, nome, cpf, email, telefone, funcao, qtd_vendas, salario, data_inicio):
        try:
            query = """
                UPDATE funcionario SET
                nome = %s, cpf = %s, email = %s, telefone = %s,
                funcao = %s, quantidade_vendas = %s, salario = %s, inicio_contrato = %s
                WHERE idfuncionario = %s
            """
            self.cursor.execute(query, (nome, cpf, email, telefone, funcao, qtd_vendas, salario, data_inicio, idfuncionario))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao alterar funcionário: {e}")

    def excluir_funcionario(self, idfuncionario):
        try:
            query = "DELETE FROM funcionario WHERE idfuncionario = %s"
            self.cursor.execute(query, (idfuncionario,))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao excluir funcionário: {e}")

    def listar_funcionarios(self):
        try:
            query = "SELECT * FROM funcionario"
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Erro ao listar funcionários: {e}")
            return []

    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
