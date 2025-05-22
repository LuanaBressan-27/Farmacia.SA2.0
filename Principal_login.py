import tkinter as tk
from tkinter import ttk
import subprocess

# Função para abrir a tela de login do administrador
def abrir_login_adm():
    root.withdraw()  # Esconde a janela principal
    subprocess.Popen(["python", "login_adm.py"])  # Executa o script do login ADM

# Função para abrir a tela de login do funcionário
def abrir_login_funcionario():
    root.withdraw()  # Esconde a janela principal
    subprocess.Popen(["python", "login_funcionario.py"])  # Executa o script do login Funcionário

# Função para abrir a tela de login do cliente
def abrir_login_cliente():
    root.withdraw()  # Esconde a janela principal
    subprocess.Popen(["python", "login_cliente.py"])  # Executa o script do login Cliente

# Função para reexibir a janela principal, caso esteja escondida
def reabrir():
    root.deiconify()  # Mostra a janela principal novamente

root = tk.Tk()  # Cria a janela principal do Tkinter

# Configurações da janela principal
root.title("Login - Sistema de Farmácia")  # Título da janela
root.geometry("400x300")  # Tamanho da janela (largura x altura)
root.configure(bg="#e6f2ff")  # Define cor de fundo (azul claro)
root.resizable(False, False)  # Impede redimensionamento da janela

# Função para fechar o programa quando o botão "Sair" for clicado
def fechar_Programa():
    root.destroy()  # Fecha a janela principal e termina o programa

# Label com mensagem de boas-vindas
tk.Label(root, text="Bem-vindo!", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=20)

# Label indicando que o usuário deve escolher o tipo de acesso
tk.Label(root, text="Escolha o tipo de acesso:", bg="#e6f2ff").pack(pady=10)

# Botão para abrir o login do ADM
ttk.Button(root, text="Login ADM", width=30, command=abrir_login_adm).pack(pady=5)

# Botão para abrir o login do Funcionário
ttk.Button(root, text="Login Funcionário", width=30, command=abrir_login_funcionario).pack(pady=5)

# Botão para abrir o login do Cliente
ttk.Button(root, text="Login Cliente", width=30, command=abrir_login_cliente).pack(pady=5)

# Botão para sair do programa
ttk.Button(root, text='Sair', width=30, command=fechar_Programa).pack(pady=5)

root.mainloop()  # Inicia o loop principal da interface gráfica
