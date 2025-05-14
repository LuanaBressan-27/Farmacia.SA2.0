import tkinter as tk
from tkinter import Menu, messagebox
from crud_funcionarios import Database as DBFunc
from crud_clientes import Database as DBCliente
from crud_produtos import read_products
from crud_fornecedores import read_suppliers

class FuncionarioRestritoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Acesso Funcionário - Consulta")
        self.root.geometry("800x600")
        self.root.configure(background="#e6f2ff")
        self.criar_menu()
        self.criar_widgets()

    def criar_menu(self):
        menu_bar = Menu(self.root)
        menu = Menu(menu_bar, tearoff=0)
        menu.add_command(label="Produtos", command=self.mostrar_produtos)
        menu.add_command(label="Fornecedores", command=self.mostrar_fornecedores)
        menu.add_command(label="Clientes", command=self.mostrar_clientes)
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

    def criar_widgets(self):
        self.text_area = tk.Text(self.root, height=30, width=100)
        self.text_area.pack(padx=10, pady=10)

    def mostrar_produtos(self):
        try:
            produtos = read_products()
            self.text_area.delete(1.0, tk.END)
            for p in produtos:
                self.text_area.insert(tk.END, f"ID: {p[0]} | Nome: {p[1]} | Tipo: {p[2]} | Quantidade: {p[3]} | Validade: {p[4]} | Fabricação: {p[5]} | Lote: {p[6]} | Fornecedor: {p[7]} | Estoque: {p[8]}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def mostrar_fornecedores(self):
        try:
            fornecedores = read_suppliers()
            self.text_area.delete(1.0, tk.END)
            for f in fornecedores:
                self.text_area.insert(tk.END, f"ID: {f[0]} | Empresa: {f[1]} | Email: {f[2]} | Telefone: {f[3]} | Produto: {f[4]} | Transporte: {f[5]} | Início: {f[6]} | Final: {f[7]}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def mostrar_clientes(self):
        try:
            db = DBCliente()
            clientes = db.listar_clientes()
            self.text_area.delete(1.0, tk.END)
            for c in clientes:
                self.text_area.insert(tk.END, f"ID: {c[0]} | Nome: {c[1]}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FuncionarioRestritoApp(root)
    root.mainloop()

