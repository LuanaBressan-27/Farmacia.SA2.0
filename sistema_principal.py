import tkinter as tk
from tkinter import ttk
import subprocess

def abrir_login_adm():
    subprocess.Popen(["python", "login_adm.py"])

def abrir_login_funcionario():
    subprocess.Popen(["python", "login_funcionario.py"])

def abrir_login_cliente():
    subprocess.Popen(["python", "login_cliente.py"])

janela = tk.Tk()
janela.title("Sistema de Farmácia - Tela Inicial")
janela.geometry("400x300")
janela.configure(bg="#e6f2ff")
janela.resizable(False, False)

tk.Label(janela, text="Bem-vindo ao Sistema de Farmácia", font=("Century Gothic", 16), bg="#cce6ff").pack(pady=20)

ttk.Button(janela, text="Entrar como ADM", width=25, command=abrir_login_adm).pack(pady=10)
ttk.Button(janela, text="Entrar como Funcionário", width=25, command=abrir_login_funcionario).pack(pady=10)
ttk.Button(janela, text="Entrar como Cliente", width=25, command=abrir_login_cliente).pack(pady=10)

janela.mainloop()