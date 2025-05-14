import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='farmacia_sa2.0'
    )

def add_product(nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO produto
        (nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque))
    conn.commit()
    cursor.close()
    conn.close()

def read_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produto")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_product(idproduto, nome_produto, tipo, quantidade_enviada, tempo_de_validade, data_de_fabricacao, lote, fornecedor, quantidade_em_estoque):
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
    cursor.close()
    conn.close()

def delete_product(idproduto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produto WHERE idproduto = %s", (idproduto,))
    conn.commit()
    cursor.close()
    conn.close()
