# Importa o conector do MySQL para Python
import mysql.connector

# Constantes com os dados de conexão com o banco de dados
MYSQL_HOST = 'localhost'       # Host do banco de dados (aqui, local)
MYSQL_USER = 'root'            # Usuário do banco
MYSQL_PASSWORD = ''            # Senha do banco (aqui está vazia)
MYSQL_DATABASE = 'farmacia_sa' # Nome do banco usado

# Função que retorna uma nova conexão com o banco de dados
def get_connection():
    # Cria e retorna uma conexão nova para cada chamada
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

# Função para adicionar um novo produto à tabela 'produto'
def add_product(nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque):
    try:
        conn = get_connection()          # Abre a conexão com o banco
        cursor = conn.cursor()           # Cria o cursor para executar comandos SQL
        
        # Query SQL para inserir dados na tabela 'produto'
        # Usa placeholders %s para evitar ataques de SQL Injection
        query = """
            INSERT INTO produto
            (nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Executa a query passando os valores dos parâmetros
        cursor.execute(query, (
            nome_produto, tipo, quantidade_enviada, tempo_de_validade,
            data_de_fabricacao, lote, fornecedor, quantidade_em_estoque
        ))
        conn.commit()  # Confirma a transação no banco, gravando os dados
    except mysql.connector.Error as e:
        # Caso haja erro no banco, relança exceção com mensagem
        raise Exception(f"Erro ao adicionar produto: {e}")
    finally:
        cursor.close()  # Fecha o cursor, liberando recurso
        conn.close()    # Fecha a conexão, liberando recurso

# Função para listar todos os produtos cadastrados no banco
def read_products():
    try:
        conn = get_connection()          # Abre conexão
        cursor = conn.cursor()           # Cria cursor
        query = "SELECT * FROM produto"  # SQL para buscar todos os produtos
        cursor.execute(query)             # Executa consulta
        result = cursor.fetchall()        # Busca todos os resultados da consulta
        return result                     # Retorna lista de produtos (tuplas)
    except mysql.connector.Error as e:
        # Captura e relança erros do banco com mensagem personalizada
        raise Exception(f"Erro ao listar produtos: {e}")
    finally:
        cursor.close()                   # Fecha cursor
        conn.close()                    # Fecha conexão

# Função para atualizar os dados de um produto já existente
def update_product(idproduto, nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque):
    try:
        conn = get_connection()          # Abre conexão
        cursor = conn.cursor()           # Cria cursor
        query = """
            UPDATE produto SET
            nome_produto = %s,
            tipo = %s,
            quantidade_enviada = %s,
            tempo_de_validade = %s,
            data_de_fabricacao = %s,
            lote = %s,
            fornecedor = %s,
            quantidade_em_estoque = %s
            WHERE idproduto = %s
        """  # Comando SQL para atualizar produto identificado por idproduto
        cursor.execute(query, (
            nome_produto, tipo, quantidade_enviada, tempo_de_validade,
            data_de_fabricacao, lote, fornecedor, quantidade_em_estoque, idproduto
        ))
        conn.commit()  # Confirma as alterações no banco
    except mysql.connector.Error as e:
        raise Exception(f"Erro ao atualizar produto: {e}")
    finally:
        cursor.close()  # Fecha cursor
        conn.close()    # Fecha conexão

# Função para deletar um produto no banco pelo seu ID
def delete_product(idproduto):
    try:
        conn = get_connection()           # Abre conexão
        cursor = conn.cursor()            # Cria cursor
        query = "DELETE FROM produto WHERE idproduto = %s"  # SQL para deletar produto por ID
        cursor.execute(query, (idproduto,))
        conn.commit()                     # Confirma exclusão no banco
    except mysql.connector.Error as e:
        raise Exception(f"Erro ao deletar produto: {e}")
    finally:
        cursor.close()  # Fecha cursor
        conn.close()    # Fecha conexão
