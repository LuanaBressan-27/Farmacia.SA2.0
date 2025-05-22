import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
from DataBase_adm import Database  # Importa a classe de conexão com o banco para o ADM

# Função para abrir a janela do menu ADM (executa outro script Python)
def abrir_menu_adm():
    subprocess.Popen(["python", "menu_adm.py"])

# Função que realiza o processo de login ADM
def login():
    nome = nome_entry.get()  # Pega o nome digitado na interface
    senha = senha_entry.get()  # Pega a senha digitada

    # Verifica se os campos foram preenchidos
    if not nome or not senha:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos")
        return

    db = Database()  # Cria instância da classe Database para o ADM

    try:
        db.connect()  # Tenta conectar ao banco de dados
    except AttributeError:
        # Caso o método connect não exista na classe, mostra erro e aborta
        messagebox.showerror("Erro", "Método 'connect' não encontrado na classe 'Database'")
        return

    if db.conn:  # Se a conexão foi estabelecida com sucesso
        try:
            # Executa consulta para verificar se usuário e senha existem na tabela 'adm'
            db.cursor.execute("SELECT * FROM adm WHERE nome = %s AND senha = %s", (nome, senha))
            resultado = db.cursor.fetchone()  # Busca o primeiro resultado da consulta

            if resultado:
                # Login válido, mostra mensagem de sucesso
                messagebox.showinfo("Sucesso", "Login ADM realizado com sucesso!")
                janela.withdraw()  # Esconde a janela atual
                abrir_menu_adm()   # Abre a janela/menu ADM
            else:
                # Login inválido, mostra mensagem de erro
                messagebox.showerror("Erro", "Usuário ou senha incorretos")

        except Exception as e:
            # Captura qualquer erro na consulta e exibe para o usuário
            messagebox.showerror("Erro de banco", str(e))

        finally:
            db.disconnect()  # Fecha a conexão com o banco

# Criação da janela principal da interface
janela = tk.Tk()
janela.title("Login ADM")
janela.geometry("400x250")
janela.configure(bg="#e6f2ff")  # Cor de fundo azul claro
janela.resizable(width=False, height=False)  # Impede redimensionamento da janela

# Label título da janela
tk.Label(janela, text="Login ADM", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=10)

# Label e campo de entrada para o nome
tk.Label(janela, text="Nome:", bg="#e6f2ff").pack()
nome_entry = ttk.Entry(janela, width=30)
nome_entry.pack(pady=5)

# Label e campo de entrada para a senha (ocultada)
tk.Label(janela, text="Senha:", bg="#e6f2ff").pack()
senha_entry = ttk.Entry(janela, width=30, show="*")
senha_entry.pack(pady=5)

# Botão para executar o login, chama a função login()
ttk.Button(janela, text="Login", command=login).pack(pady=10)

# Função para voltar à tela principal (fecha esta janela e abre a outra)
def retornar():
    janela.withdraw()  # Esconde esta janela
    subprocess.Popen(["python", "Principal_login.py"])  # Abre a tela principal

# Botão para voltar à tela principal
ttk.Button(janela, text="Voltar", command=retornar).pack(pady=1)

# Mantém a janela aberta e em loop
janela.mainloop()
