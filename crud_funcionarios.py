import mysql.connector  # Importa o módulo de conexão com o banco de dados MySQL

class Database:
    def __init__(self):
        # Método construtor: chamado automaticamente ao criar uma instância da classe
        try:
            self.connection = mysql.connector.connect(
                host="localhost",       # Endereço do servidor
                user="root",            # Usuário do banco
                password="",            # Senha do banco (vazia neste caso)
                database="farmacia_sa"  # Nome do banco de dados
            )
            # Verifica se a conexão foi bem-sucedida
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()  # Cria o cursor para executar comandos SQL
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.connection = None  # Define como None se a conexão falhar
            self.cursor = None

    def inserir_funcionario(self, nome, cpf, email, telefone, funcao, qtd_vendas, salario, inicio_contrato):
        # Insere um novo funcionário na tabela
        try:
            query = """
                INSERT INTO funcionario
                (nome, cpf, email, telefone, funcao, quantidade_vendas, salario, inicio_contrato)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (nome, cpf, email, telefone, funcao, qtd_vendas, salario, inicio_contrato))
            self.connection.commit()  # Salva as alterações no banco
        except mysql.connector.Error as e:
            raise Exception(f"Erro ao inserir funcionário: {e}")  # Lança exceção com mensagem descritiva

    def alterar_funcionario(self, idfuncionario, nome, cpf, email, telefone, funcao, qtd_vendas, salario, inicio_contrato):
        # Atualiza os dados de um funcionário existente
        try:
            query = """
                UPDATE funcionario SET
                nome = %s, cpf = %s, email = %s, telefone = %s,
                funcao = %s, quantidade_vendas = %s, salario = %s, inicio_contrato = %s
                WHERE idfuncionario = %s
            """
            self.cursor.execute(query, (nome, cpf, email, telefone, funcao, qtd_vendas, salario, inicio_contrato, idfuncionario))
            self.connection.commit()
        except mysql.connector.Error as e:
            raise Exception(f"Erro ao alterar funcionário: {e}")

    def excluir_funcionario(self, idfuncionario):
        # Exclui um funcionário com base no ID
        try:
            query = "DELETE FROM funcionario WHERE idfuncionario = %s"
            self.cursor.execute(query, (idfuncionario,))
            self.connection.commit()
        except mysql.connector.Error as e:
            raise Exception(f"Erro ao excluir funcionário: {e}")

    def listar_funcionarios(self):
        # Retorna todos os registros da tabela de funcionários
        try:
            query = "SELECT * FROM funcionario"
            self.cursor.execute(query)
            return self.cursor.fetchall()  # Retorna os resultados como uma lista de tuplas
        except mysql.connector.Error as e:
            raise Exception(f"Erro ao listar funcionários: {e}")

    def verificar_login(self, nome, email):
        # Verifica se existe um funcionário com nome e e-mail informados (simples verificação de login)
        try:
            query = "SELECT * FROM funcionario WHERE nome = %s AND email = %s"
            self.cursor.execute(query, (nome, email))
            return self.cursor.fetchone()  # Retorna o primeiro registro encontrado, ou None
        except mysql.connector.Error as e:
            raise Exception(f"Erro ao verificar login: {e}")

    def fechar_conexao(self):
        # Fecha o cursor e a conexão com o banco de dados
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
