import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DATABASE = 'farmacia_sa2.0'

def get_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

def add_supplier(nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO fornecedor
        (nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato))
    conn.commit()
    cursor.close()
    conn.close()

def read_suppliers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM fornecedor")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_supplier(idfornecedor, nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato):
    conn = get_connection()
    cursor = conn.cursor()
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
    """
    cursor.execute(query, (nome_empresa, email, telefone, produto, transporte, inicio_contrato, final_contrato, idfornecedor))
    conn.commit()
    cursor.close()
    conn.close()

def delete_supplier(idfornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM fornecedor WHERE idfornecedor = %s", (idfornecedor,))
    conn.commit()
    cursor.close()
    conn.close()
