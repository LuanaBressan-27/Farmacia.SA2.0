import tkinter as tk
from tkinter import ttk

def abrir_menu_adm(janela_principal):
    janela = tk.Toplevel()
    janela.title("Menu ADM")
    janela.geometry("400x300")
    janela.configure(bg="#e6f2ff")
    janela.resizable(False, False)

    def voltar():
        janela.destroy()
        janela_principal.deiconify()

    tk.Label(janela, text="Menu do Administrador", font=("Arial", 16), bg="#e6f2ff").pack(pady=20)

    # Aqui você pode adicionar mais botões para funcionalidades do ADM
    ttk.Button(janela, text="Voltar", command=voltar).pack(pady=20)
