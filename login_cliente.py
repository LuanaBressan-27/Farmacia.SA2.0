import tkinter as tk
from tkinter import ttk, messagebox
from crud_clientes import Database  # Importa a classe para acesso ao banco de clientes
import subprocess  # Para abrir outros scripts Python

# Função para abrir o menu do cliente (executa outro script)
def abrir_menu_cliente():
    subprocess.Popen(["python", "menu_cliente.py"])

# Função para realizar o login do cliente
def login():
    nome = nome_entry.get()  # Captura o nome digitado
    senha = senha_entry.get()  # Captura a senha digitada

    # Verifica se os campos foram preenchidos
    if not nome or not senha:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos")
        return

    try:
        db = Database()  # Instancia o objeto Database para acesso aos dados do cliente
        clientes = db.listar_clientes()  # Recupera todos os clientes cadastrados

        # Percorre a lista de clientes para verificar se nome e senha conferem
        for c in clientes:
            if c[1] == nome and c[2] == senha:  # Assumindo que c[1] é nome e c[2] é senha
                messagebox.showinfo("Sucesso", "Login Cliente realizado com sucesso!")
                janela.withdraw()  # Esconde a janela atual
                abrir_menu_cliente()  # Abre o menu do cliente
                return  # Sai da função após sucesso

        # Se não achou nenhum cliente com esse nome e senha, mostra erro
        messagebox.showerror("Erro", "Nome ou senha incorretos")

    except Exception as e:
        # Captura qualquer erro e mostra para o usuário
        messagebox.showerror("Erro", str(e))

# Configuração da janela principal do login cliente
janela = tk.Tk()
janela.title("Login Cliente")
janela.geometry("400x250")
janela.configure(bg="#e6f2ff")  # Cor de fundo azul claro
janela.resizable(width=False, height=False)  # Impede redimensionamento

# Label título
tk.Label(janela, text="Login Cliente", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=10)

# Label e entrada para nome
tk.Label(janela, text="Nome:", bg="#e6f2ff").pack()
nome_entry = ttk.Entry(janela, width=30)
nome_entry.pack(pady=5)

# Label e entrada para senha (ocultada)
tk.Label(janela, text="Senha:", bg="#e6f2ff").pack()
senha_entry = ttk.Entry(janela, width=30, show="*")
senha_entry.pack(pady=5)

# Botão para realizar login
ttk.Button(janela, text="Login", command=login).pack(pady=10)

# Função para voltar para a tela principal
def retornar():
    janela.withdraw()  # Esconde esta janela
    subprocess.Popen(["python", "Principal_login.py"])  # Abre a tela principal

# Botão para voltar à tela principal
ttk.Button(janela, text="Voltar", command=retornar).pack(pady=1)

# Mantém a janela aberta
janela.mainloop()
