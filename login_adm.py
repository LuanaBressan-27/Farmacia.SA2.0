import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
import subprocess

def abrir_menu_adm():
    subprocess.Popen(["python", "menu_adm.py"])

def login():
    nome = nome_entry.get()
    senha = senha_entry.get()

    if not nome or not senha:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="farmacia_sa2_0"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM adm WHERE nome = %s AND senha = %s", (nome, senha))
        resultado = cursor.fetchone()

        if resultado:
            messagebox.showinfo("Sucesso", "Login ADM realizado com sucesso!")
            janela.destroy()
            abrir_menu_adm()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    except Exception as e:
        messagebox.showerror("Erro de banco", str(e))

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

janela = tk.Tk()
janela.title("Login ADM")
janela.geometry("400x250")
janela.configure(bg="#e6f2ff")

tk.Label(janela, text="Login ADM", font=("Century Gothic", 20), bg="#cce6ff").pack(pady=10)
tk.Label(janela, text="Nome:", bg="#e6f2ff").pack()
nome_entry = ttk.Entry(janela, width=30)
nome_entry.pack(pady=5)

tk.Label(janela, text="Senha:", bg="#e6f2ff").pack()
senha_entry = ttk.Entry(janela, width=30, show="*")
senha_entry.pack(pady=5)

ttk.Button(janela, text="Login", command=login).pack(pady=20)

janela.mainloop()

