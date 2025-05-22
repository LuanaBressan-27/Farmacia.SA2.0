import tkinter as tk
from tkinter import ttk
import subprocess

janela = tk.Tk()

# Garantir que a janela esteja visível ao iniciar
janela.deiconify()  # Exibe a janela, caso estivesse oculta

# Configurações da janela principal
janela.title("Menu Funcionário")
janela.geometry("300x200")
janela.configure(bg="#e6f2ff")  # Cor de fundo azul claro
janela.resizable(width=False, height=False)  # Janela com tamanho fixo

def retornar():
    # Função para esconder a janela atual e abrir a tela de login do funcionário
    janela.withdraw()  # Esconde a janela sem fechar
    subprocess.Popen(["python", "login_funcionario.py"])  # Abre a tela de login do funcionário

def abrir_interface():
    # Função para fechar a janela atual e abrir a tela restrita do funcionário
    janela.destroy()  # Fecha a janela atual
    subprocess.Popen(["python", "tela_funcionario_restrita.py"])  # Abre a tela restrita do funcionário

# Botão que chama a função para abrir o sistema
ttk.Button(janela, text="Abrir Sistema", command=abrir_interface).pack(pady=50)

# Botão para desconectar e voltar ao login
ttk.Button(janela, text="Desconectar", command=retornar).pack(pady=10)

janela.mainloop()
