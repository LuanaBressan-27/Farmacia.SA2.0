import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
from DataBase_adm import Database

def abrir_menu_adm():
    subprocess.Popen(["python", "menu_adm.py"])

def login():
    nome = nome_entry.get()
    senha = senha_entry.get()

    if not nome or not senha:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos")
        return

    db = Database()
    try:
        db.connect()
    except AttributeError:
        messagebox.showerror("Erro", "Método 'connect' não encontrado na classe 'Database'")
        return

    if db.conn:
        try:
            db.cursor.execute("SELECT * FROM adm WHERE nome = %s AND senha = %s", (nome, senha))
            resultado = db.cursor.fetchone()

            if resultado:
                messagebox.showinfo("Sucesso", "Login ADM realizado com sucesso!")
                janela.withdraw()
                abrir_menu_adm()
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos")

        except Exception as e:
            messagebox.showerror("Erro de banco", str(e))

        finally:
            db.disconnect()

janela = tk.Tk()
janela.title("Login ADM")
janela.geometry("400x250")
janela.configure(bg="#e6f2ff")
janela.resizable(width=False, height=False)

tk.Label(janela, text="Login ADM", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=10)
tk.Label(janela, text="Nome:", bg="#e6f2ff").pack()
nome_entry = ttk.Entry(janela, width=30)
nome_entry.pack(pady=5)

tk.Label(janela, text="Senha:", bg="#e6f2ff").pack()
senha_entry = ttk.Entry(janela, width=30, show="*")
senha_entry.pack(pady=5)

ttk.Button(janela, text="Login", command=login).pack(pady=10)
def retornar():
    janela.withdraw()
    subprocess.Popen(["python", "Principal_login.py"])
ttk.Button(janela, text="Voltar",command=retornar).pack(pady=1)

janela.mainloop()
