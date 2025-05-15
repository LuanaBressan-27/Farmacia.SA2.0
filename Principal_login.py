import tkinter as tk
from tkinter import ttk
import subprocess

def abrir_login_adm():
    root.withdraw()
    subprocess.Popen(["python", "login_adm.py"])
    
def abrir_login_funcionario():
    root.withdraw()
    subprocess.Popen(["python", "login_funcionario.py"])

def abrir_login_cliente():
    root.withdraw()
    subprocess.Popen(["python", "login_cliente.py"])

def reabrir():
    root.deiconify
root = tk.Tk()
if root == root.withdraw:
    root.deiconify
root.title("Login - Sistema de Farmácia")
root.geometry("400x300")
root.configure(bg="#e6f2ff")
root.resizable(False, False)

tk.Label(root, text="Bem-vindo!", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=20)
tk.Label(root, text="Escolha o tipo de acesso:", bg="#e6f2ff").pack(pady=10)

ttk.Button(root, text="Login ADM", width=30, command=abrir_login_adm).pack(pady=5)
ttk.Button(root, text="Login Funcionário", width=30, command=abrir_login_funcionario).pack(pady=5)
ttk.Button(root, text="Login Cliente", width=30, command=abrir_login_cliente).pack(pady=5)

root.mainloop()
