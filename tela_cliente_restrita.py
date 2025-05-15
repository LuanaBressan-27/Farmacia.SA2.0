import tkinter as tk
from tkinter import Menu, messagebox
from crud_produtos import read_products
import subprocess

class ClienteRestritoApp:
    def __init__(self, root):
        self.root = root
        if root == root.withdraw:
            root.deiconify
        self.root.title("Acesso Cliente - Produtos Disponíveis")
        self.root.geometry("800x600")
        self.root.configure(background="#e6f2ff")
        root.resizable(width=False, height=False)
        self.criar_menu()
        self.criar_widgets()

    def criar_menu(self):
        menu_bar = Menu(self.root)
        menu = Menu(menu_bar, tearoff=0)
        menu.add_command(label="Ver Produtos", command=self.mostrar_produtos)
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

    def criar_widgets(self):
        self.text_area = tk.Text(self.root, height=30, width=100)
        self.text_area.pack(padx=10, pady=10)
        tk.Button(root, text="Voltar",command=retornar).pack(padx=10)

    def mostrar_produtos(self):
        try:
            produtos = read_products()
            self.text_area.delete(1.0, tk.END)
            for p in produtos:
                self.text_area.insert(tk.END, f"ID: {p[0]} | Nome: {p[1]} | Tipo: {p[2]} | Quantidade: {p[3]} | Validade: {p[4]} | Fabricação: {p[5]} | Lote: {p[6]} | Fornecedor: {p[7]} | Estoque: {p[8]}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))
def retornar():
    root.withdraw()
    subprocess.Popen(["python", "menu_funcionario.py"])
if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteRestritoApp(root)
    root.mainloop()

