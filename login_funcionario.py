import tkinter as tk
from tkinter import ttk, messagebox
from crud_funcionarios import Database
import subprocess

def abrir_menu_funcionario():
    subprocess.Popen(["python", "menu_funcionario.py"])

def login():
    nome = nome_entry.get()
    email = email_entry.get()

    if not nome or not email:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos")
        return

    try:
        db = Database()
        resultado = db.verificar_login(nome, email)
        if resultado:
            messagebox.showinfo("Sucesso", "Login Funcionário realizado com sucesso!")
            janela.destroy()
            abrir_menu_funcionario()
        else:
            messagebox.showerror("Erro", "Nome ou e-mail incorretos")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

janela = tk.Tk()
janela.title("Login Funcionário")
janela.geometry("400x250")
janela.configure(bg="#e6f2ff")
janela.resizable(width=False, height=False)

tk.Label(janela, text="Login Funcionário", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=10)
tk.Label(janela, text="Nome:", bg="#e6f2ff").pack()
nome_entry = ttk.Entry(janela, width=30)
nome_entry.pack(pady=5)

tk.Label(janela, text="Email:", bg="#e6f2ff").pack()
email_entry = ttk.Entry(janela, width=30)
email_entry.pack(pady=5)

ttk.Button(janela, text="Login", command=login).pack(pady=10)
def retornar():
    janela.destroy()
    import Principal_login
ttk.Button(janela, text="Voltar",command=retornar).pack(pady=1)

janela.mainloop()
