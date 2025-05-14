import tkinter as tk
from tkinter import ttk
import subprocess

jan_botao = tk.Tk()
jan_botao.title("Menu Principal - Cliente")
jan_botao.geometry("600x300")
jan_botao.configure(background="#e6f2ff")
jan_botao.resizable(width=False, height=False)

titulo = tk.Label(jan_botao, text="Menu Principal - Cliente", font=("Century Gothic", 20), bg="#cce6ff", fg="black")
titulo.pack(pady=20)

def abrir_interface():
    subprocess.Popen(["python", "tela_cliente_restrita.py"])

ttk.Button(jan_botao, text="Visualizar Produtos", width=25, command=abrir_interface).pack(pady=20)

jan_botao.mainloop()

