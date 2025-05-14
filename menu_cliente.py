import tkinter as tk
from tkinter import ttk
import subprocess

janela = tk.Tk()
janela.title("Menu Cliente")
janela.geometry("300x200")
janela.configure(bg="#e6f2ff")

def abrir_interface(): subprocess.Popen(["python", "tela_cliente_restrita.py"])
ttk.Button(janela, text="Visualizar Produtos", command=abrir_interface).pack(pady=50)

janela.mainloop()

