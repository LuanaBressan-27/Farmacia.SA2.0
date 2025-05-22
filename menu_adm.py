import tkinter as tk
from tkinter import ttk
import subprocess  # Para executar outros scripts Python

# Criação da janela principal do menu ADM
janela = tk.Tk()
janela.title("Menu ADM")  # Título da janela
janela.geometry("400x250")  # Tamanho fixo da janela
janela.configure(bg="#e6f2ff")  # Cor de fundo azul claro
janela.resizable(width=False, height=False)  # Janela não pode ser redimensionada

# Função para "desconectar" e voltar para a tela de login do ADM
def retornar():
    janela.withdraw()  # Esconde a janela atual
    subprocess.Popen(["python", "login_adm.py"])  # Abre o script de login ADM

# Função para abrir a tela de gerenciamento de produtos
def abrir_produto():
    janela.destroy()  # Fecha a janela atual para evitar janelas abertas em excesso
    subprocess.Popen(["python", "tela_produto_adm.py"])  # Abre o script da tela de produto

# Função para abrir a tela de gerenciamento de funcionários
def abrir_funcionario():
    subprocess.Popen(["python", "tela_funcionario_adm.py"])  # Abre a tela de funcionário
    janela.destroy()  # Fecha a janela atual

# Função para abrir a tela de gerenciamento de fornecedores
def abrir_fornecedor():
    subprocess.Popen(["python", "tela_fornecedor_adm.py"])  # Abre a tela de fornecedor
    janela.destroy()  # Fecha a janela atual

# Função para abrir a tela de gerenciamento de clientes
def abrir_cliente():
    subprocess.Popen(["python", "tela_cliente_adm.py"])  # Abre a tela de cliente
    janela.destroy()  # Fecha a janela atual

# Botões para cada funcionalidade, com espaçamento vertical (pady)
ttk.Button(janela, text="Produtos", command=abrir_produto).pack(pady=10)
ttk.Button(janela, text="Funcionários", command=abrir_funcionario).pack(pady=10)
ttk.Button(janela, text="Fornecedores", command=abrir_fornecedor).pack(pady=10)
ttk.Button(janela, text="Clientes", command=abrir_cliente).pack(pady=10)
ttk.Button(janela, text="Desconectar", command=retornar).pack(pady=10)

# Mantém a janela aberta até que o usuário a feche
janela.mainloop()
