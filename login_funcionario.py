import tkinter as tk
from tkinter import ttk, messagebox
from crud_funcionarios import Database  # Importa a classe de acesso ao banco para funcionários
import subprocess  # Para abrir outros scripts

# Função para reabrir a janela (não usada no código atual)
def reabrir():
    janela.deiconify()  # Atenção: falta os parênteses para chamar o método, deveria ser janela.deiconify()

# Função que abre o menu do funcionário (executa outro script)
def abrir_menu_funcionario():
    subprocess.Popen(["python", "menu_funcionario.py"])

# Função para realizar login do funcionário
def login():
    nome = nome_entry.get()  # Pega o nome digitado
    email = email_entry.get()  # Pega o email digitado

    # Verifica se campos estão preenchidos
    if not nome or not email:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos")
        return

    try:
        db = Database()  # Cria instância do DB
        resultado = db.verificar_login(nome, email)  # Consulta no banco se existe funcionário com esse nome e email
        if resultado:
            messagebox.showinfo("Sucesso", "Login Funcionário realizado com sucesso!")
            janela.withdraw()  # Esconde janela de login
            abrir_menu_funcionario()  # Abre o menu do funcionário
        else:
            messagebox.showerror("Erro", "Nome ou e-mail incorretos")
    except Exception as e:
        messagebox.showerror("Erro", str(e))  # Mostra erro na interface

# Configuração da janela principal
janela = tk.Tk()
janela.title("Login Funcionário")
janela.geometry("400x250")
janela.configure(bg="#e6f2ff")  # Cor de fundo azul claro
janela.resizable(width=False, height=False)

# Label título
tk.Label(janela, text="Login Funcionário", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=10)

# Label e entrada para nome
tk.Label(janela, text="Nome:", bg="#e6f2ff").pack()
nome_entry = ttk.Entry(janela, width=30)
nome_entry.pack(pady=5)

# Label e entrada para email
tk.Label(janela, text="Email:", bg="#e6f2ff").pack()
email_entry = ttk.Entry(janela, width=30)
email_entry.pack(pady=5)

# Botão para login
ttk.Button(janela, text="Login", command=login).pack(pady=10)

# Função para voltar para a tela principal
def voltar():
    janela.destroy()  # Fecha a janela atual
    subprocess.Popen(["python", "Principal_login.py"])  # Abre a tela principal

# Botão para voltar
ttk.Button(janela, text="Voltar", command=voltar).pack(pady=1)

# Mantém a janela aberta
janela.mainloop()
