import tkinter as tk
from tkinter import ttk
import subprocess

janela = tk.Tk()
janela.title("Menu ADM")
janela.geometry("400x250")
janela.configure(bg="#e6f2ff")
janela.resizable(width=False, height=False)
def retornar():
    janela.withdraw()
    subprocess.Popen(["python", "login_adm.py"])

def abrir_produto():
    janela.destroy ()
    subprocess.Popen(["python", "tela_produto_adm.py"])
def abrir_funcionario(): 
    subprocess.Popen(["python", "tela_funcionario_adm.py"])
    janela.destroy ()
def abrir_fornecedor(): 
    subprocess.Popen(["python", "tela_fornecedor_adm.py"])
    janela.destroy ()
def abrir_cliente(): 
    subprocess.Popen(["python", "tela_cliente_adm.py"])
    janela.destroy ()

ttk.Button(janela, text="Produtos", command=abrir_produto).pack(pady=10)
ttk.Button(janela, text="Funcionários", command=abrir_funcionario).pack(pady=10)
ttk.Button(janela, text="Fornecedores", command=abrir_fornecedor).pack(pady=10)
ttk.Button(janela, text="Clientes", command=abrir_cliente).pack(pady=10)
ttk.Button(janela, text="Desconectar",command=retornar).pack(pady=10)

janela.mainloop()
