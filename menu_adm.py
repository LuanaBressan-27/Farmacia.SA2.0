import tkinter as tk
from tkinter import ttk
import subprocess

janela = tk.Tk()
janela.title("Menu ADM")
janela.geometry("400x300")
janela.configure(bg="#e6f2ff")

def abrir_produto(): subprocess.Popen(["python", "tela_produto_adm.py"])
def abrir_funcionario(): subprocess.Popen(["python", "tela_funcionario_adm.py"])
def abrir_fornecedor(): subprocess.Popen(["python", "tela_fornecedor_adm.py"])
def abrir_cliente(): subprocess.Popen(["python", "tela_cliente_adm.py"])

ttk.Button(janela, text="Produtos", command=abrir_produto).pack(pady=10)
ttk.Button(janela, text="Funcionários", command=abrir_funcionario).pack(pady=10)
ttk.Button(janela, text="Fornecedores", command=abrir_fornecedor).pack(pady=10)
ttk.Button(janela, text="Clientes", command=abrir_cliente).pack(pady=10)

janela.mainloop()
