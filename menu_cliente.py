import tkinter as tk
from tkinter import ttk
import subprocess  # Para abrir outros scripts Python

# Cria a janela principal do Menu Cliente
janela = tk.Tk()
janela.title("Menu Cliente")            # Define o título da janela
janela.geometry("300x200")              # Define o tamanho da janela
janela.configure(bg="#e6f2ff")          # Define a cor de fundo (azul claro)
janela.resizable(width=False, height=False)  # Impede redimensionamento da janela

# Função para desconectar e voltar para a tela de login do cliente
def retornar():
    janela.destroy()  # Fecha a janela atual
    subprocess.Popen(["python", "login_cliente.py"])  # Abre o script da tela de login do cliente

# Função para abrir a interface restrita do cliente (ex: visualizar produtos)
def abrir_interface():
    janela.destroy()  # Fecha a janela atual
    subprocess.Popen(["python", "tela_cliente_restrita.py"])  # Abre a tela restrita do cliente

# Botão para visualizar produtos, com espaçamento vertical (pady)
ttk.Button(janela, text="Visualizar Produtos", command=abrir_interface).pack(pady=50)

# Botão para desconectar e voltar ao login, com espaçamento menor
ttk.Button(janela, text="Desconectar", command=retornar).pack(pady=10)

# Mantém a janela aberta até o usuário fechá-la
janela.mainloop()
