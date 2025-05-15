import tkinter as tk
from tkinter import ttk, messagebox
from DataBase_adm import Database
import menu_adm

def abrir_janela_login_adm(janela_principal):
    janela = tk.Toplevel()
    janela.title("Login ADM")
    janela.geometry("300x200")
    janela.configure(bg="#e6f2ff")
    janela.resizable(False, False)

    def voltar():
        janela.destroy()
        janela_principal.deiconify()

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
            db.cursor.execute("SELECT * FROM adm WHERE nome = %s AND senha = %s", (nome, senha))
            resultado = db.cursor.fetchone()

            if resultado:
                messagebox.showinfo("Sucesso", "Login ADM realizado com sucesso!")
                janela.destroy()
                menu_adm.abrir_menu_adm(janela_principal)
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos")

    tk.Label(janela, text="Usuário:", bg="#e6f2ff").pack(pady=5)
    nome_entry = ttk.Entry(janela, width=30)
    nome_entry.pack()

    tk.Label(janela, text="Senha:", bg="#e6f2ff").pack(pady=5)
    senha_entry = ttk.Entry(janela, show="*", width=30)
    senha_entry.pack()

    ttk.Button(janela, text="Entrar", command=login).pack(pady=10)
    ttk.Button(janela, text="Voltar", command=voltar).pack()
