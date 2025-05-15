import tkinter as tk
from tkinter import ttk
import subprocess

janela = tk.Tk()
janela.title("Menu Funcionário")
janela.geometry("300x200")
janela.configure(bg="#e6f2ff")
janela.resizable(width=False, height=False)
def retornar():
    janela.delete()
    import login_funcionario

def abrir_interface(): 
    janela.delete()
    subprocess.Popen(["python", "tela_funcionario_restrita.py"])
ttk.Button(janela, text="Abrir Sistema", command=abrir_interface).pack(pady=50)
ttk.Button(janela, text="Voltar",command=retornar).pack(pady=10)

janela.mainloop()
