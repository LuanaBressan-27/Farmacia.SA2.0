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

def add_product(produto, quantidade, valor, fornecedor, descricao, validade):
    conn = get_connection()
    cursor = conn.cursor()
    # Ordem dos valores corrigida
    query = "INSERT INTO produto (produto, quantidade, valor, fornecedor, descricao, validade) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (produto, quantidade, valor, fornecedor, descricao, validade))
    conn.commit()
    cursor.close()
    conn.close()

def read_products():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM produto"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_product(produto, quantidade, valor, fornecedor, descricao, validade, idproduto):
    conn = get_connection()
    cursor = conn.cursor()
    # Nome da coluna corrigido para "descricao"
    query = "UPDATE produto SET produto=%s, quantidade=%s, valor=%s, fornecedor=%s, descricao=%s, validade=%s WHERE idproduto=%s"
    cursor.execute(query, (produto, quantidade, valor, fornecedor, descricao, validade, idproduto))
    conn.commit()
    cursor.close()
    conn.close()

def delete_product(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM produto WHERE idproduto=%s"
    cursor.execute(query, (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
