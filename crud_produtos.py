import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DATABASE = 'farmacia_sa'

def get_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

def add_product(nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO produto
            (nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque))
        conn.commit()
    except mysql.connector.Error as e:
        raise Exception(f"Erro ao adicionar produto: {e}")
    finally:
        cursor.close()
        conn.close()

def read_products():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM produto"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as e:
        raise Exception(f"Erro ao listar produtos: {e}")
    finally:
        cursor.close()
        conn.close()

def update_product(idproduto, nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque):
    try:
        conn = get_connection()
        cursor = conn.cursor()
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
        """
        cursor.execute(query, (nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque, idproduto))
        conn.commit()
    except mysql.connector.Error as e:
        raise Exception(f"Erro ao atualizar produto: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_product(idproduto):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM produto WHERE idproduto = %s"
        cursor.execute(query, (idproduto,))
        conn.commit()
    except mysql.connector.Error as e:
        raise Exception(f"Erro ao deletar produto: {e}")
    finally:
        cursor.close()
        conn.close()
