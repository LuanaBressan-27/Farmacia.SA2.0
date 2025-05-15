import tkinter as tk
from tkinter import ttk
import subprocess

janela = tk.Tk()
janela.title("Menu Cliente")
janela.geometry("300x200")
janela.configure(bg="#e6f2ff")
janela.resizable(width=False, height=False)
def retornar():
    janela.destroy()
    import login_cliente

def abrir_interface(): 
    janela.destroy()
    subprocess.Popen(["python", "tela_cliente_restrita.py"])
ttk.Button(janela, text="Visualizar Produtos", command=abrir_interface).pack(pady=50)
ttk.Button(janela, text="Voltar",command=retornar).pack(pady=10)

janela.mainloop()

