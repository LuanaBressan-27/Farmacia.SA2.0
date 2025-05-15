import tkinter as tk
from tkinter import ttk, messagebox
from crud_clientes import Database
import subprocess

def abrir_menu_cliente():
    subprocess.Popen(["python", "menu_cliente.py"])

def login():
    nome = nome_entry.get()
    senha = senha_entry.get()

    if not nome or not senha:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos")
        return

    try:
        db = Database()
        clientes = db.listar_clientes()
        for c in clientes:
            if c[1] == nome and c[2] == senha:
                messagebox.showinfo("Sucesso", "Login Cliente realizado com sucesso!")
                janela.destroy()
                abrir_menu_cliente()
                return
        messagebox.showerror("Erro", "Nome ou senha incorretos")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

janela = tk.Tk()
janela.title("Login Cliente")
janela.geometry("400x250")
janela.configure(bg="#e6f2ff")
janela.resizable(width=False, height=False)

tk.Label(janela, text="Login Cliente", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=10)
tk.Label(janela, text="Nome:", bg="#e6f2ff").pack()
nome_entry = ttk.Entry(janela, width=30)
nome_entry.pack(pady=5)

tk.Label(janela, text="Senha:", bg="#e6f2ff").pack()
senha_entry = ttk.Entry(janela, width=30, show="*")
senha_entry.pack(pady=5)

ttk.Button(janela, text="Login", command=login).pack(pady=10)
def retornar():
    janela.destroy()
    import Principal_login
ttk.Button(janela, text="Voltar",command=retornar).pack(pady=1)

janela.mainloop()


