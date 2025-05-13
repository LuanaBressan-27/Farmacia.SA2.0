import mysql.connector

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Substitua pelo seu usuário
                password="",  # Substitua pela sua senha
                database="farmacia_sa"
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.connection = None
            self.cursor = None

    def inserir_funcionario(self, nome, email, telefone, cidade, estado, bairro, data_de_nascimento, data_de_contrato):
        try:
            query = """
                INSERT INTO funcionario 
                (nome, email, telefone, cidade, estado, bairro, data_de_nascimento, data_de_contrato)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (nome, email, telefone, cidade, estado, bairro, data_de_nascimento, data_de_contrato))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao inserir funcionário: {e}")

    def alterar_funcionario(self, idfuncionario, nome, email, telefone, cidade, estado, bairro, data_de_nascimento, data_de_contrato):
        try:
            query = """
                UPDATE funcionario SET 
                nome = %s, email = %s, telefone = %s, cidade = %s, estado = %s, bairro = %s, 
                data_de_nascimento = %s, data_de_contrato = %s 
                WHERE idfuncionario = %s
            """
            self.cursor.execute(query, (nome, email, telefone, cidade, estado, bairro, data_de_nascimento, data_de_contrato, idfuncionario))
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

    def verificar_login(self, nome, email):
        try:
            query = """
                SELECT * FROM funcionario 
                WHERE nome = %s AND email = %s
            """
            self.cursor.execute(query, (nome, email))
            resultado = self.cursor.fetchone()
            if resultado:
                return True  # Login válido
            else:
                return False  # Login inválido
        except mysql.connector.Error as e:
            print(f"Erro ao verificar login: {e}")
            return None

    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
