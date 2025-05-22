# Importa o módulo necessário para conectar com o MySQL
import mysql.connector

# Constantes com os dados de acesso ao banco de dados
MYSQL_HOST = 'localhost'        # Endereço do servidor MySQL
MYSQL_USER = 'root'             # Nome de usuário do banco
MYSQL_PASSWORD = ''             # Senha do banco (vazia neste caso)
MYSQL_DATABASE = 'farmacia_sa'  # Nome do banco de dados utilizado

# Função que cria e retorna uma conexão com o banco de dados
def get_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

# Função que adiciona um novo fornecedor ao banco de dados
def add_supplier(nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato):
    conn = get_connection()           # Abre a conexão com o banco
    cursor = conn.cursor()            # Cria um cursor para executar comandos SQL
    query = """
        INSERT INTO fornecedor
        (nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """  # Comando SQL com placeholders (%s) para evitar SQL Injection
    # Executa o comando com os valores fornecidos como parâmetros
    cursor.execute(query, (nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato))
    conn.commit()     # Salva (confirma) a transação no banco
    cursor.close()    # Fecha o cursor para liberar recursos
    conn.close()      # Fecha a conexão com o banco

# Função que retorna todos os fornecedores cadastrados
def read_suppliers():
    conn = get_connection()      # Abre a conexão
    cursor = conn.cursor()       # Cria o cursor
    cursor.execute("SELECT * FROM fornecedor")  # Executa a consulta para buscar todos os registros
    result = cursor.fetchall()   # Recupera todos os resultados como lista de tuplas
    cursor.close()               # Fecha o cursor
    conn.close()                 # Fecha a conexão
    return result                # Retorna os dados encontrados

# Função que atualiza os dados de um fornecedor existente
def update_supplier(idfornecedor, nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato):
    conn = get_connection()       # Abre a conexão
    cursor = conn.cursor()        # Cria o cursor
    query = """
        UPDATE fornecedor SET
        nome_empresa = %s,
        email = %s,
        telefone = %s,
        produto = %s,
        transporte = %s,
        inicio_contrato = %s,
        final_contrato = %s
        WHERE idfornecedor = %s
    """  # Comando SQL para atualizar fornecedor com base no ID
    # Executa a atualização com os novos valores
    cursor.execute(query, (nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato, idfornecedor))
    conn.commit()     # Confirma as alterações
    cursor.close()    # Fecha o cursor
    conn.close()      # Fecha a conexão

# Função que exclui um fornecedor pelo ID
def delete_supplier(idfornecedor):
    conn = get_connection()                        # Abre a conexão
    cursor = conn.cursor()                         # Cria o cursor
    cursor.execute("DELETE FROM fornecedor WHERE idfornecedor = %s", (idfornecedor,))  # Comando SQL para deletar
    conn.commit()     # Confirma a exclusão
    cursor.close()    # Fecha o cursor
    conn.close()      # Fecha a conexão
