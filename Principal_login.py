import tkinter as tk
from tkinter import ttk
import login_adm

def abrir_login_adm():
    root.withdraw()
    login_adm.abrir_janela_login_adm(root)

root = tk.Tk()
root.title("Login - Sistema de Farmácia")
root.geometry("400x300")
root.configure(bg="#e6f2ff")
root.resizable(False, False)

tk.Label(root, text="Bem-vindo!", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=20)
tk.Label(root, text="Escolha o tipo de acesso:", bg="#e6f2ff").pack(pady=10)

ttk.Button(root, text="Login ADM", width=30, command=abrir_login_adm).pack(pady=5)

# Adicione outros botões se necessário

root.mainloop()
