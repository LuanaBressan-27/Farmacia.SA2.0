import tkinter as tk
from tkinter import ttk, messagebox, Menu
from crud_clientes import Database

class ClienteADMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Clientes - ADM")
        self.root.geometry("600x500")
        self.root.configure(background="#e6f2ff")
        self.db = Database()

        self.criar_menu()
        self.criar_widgets()

    def criar_menu(self):
        menu_bar = Menu(self.root)
        menu = Menu(menu_bar, tearoff=0)
        menu.add_command(label="Produtos")
        menu.add_command(label="Funcionários")
        menu.add_command(label="Fornecedores")
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

    def criar_widgets(self):
        labels = ["ID", "Nome de Usuário", "Senha"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self.root, text=label + ":", bg="#e6f2ff").grid(row=i, column=0, padx=10, pady=10, sticky="e")
            entry = tk.Entry(self.root, width=40)
            if "senha" in label.lower():
                entry.config(show="*")
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.entries[label.lower().split()[0]] = entry

        ttk.Button(self.root, text="Cadastrar", command=self.cadastrar).grid(row=3, column=0)
        ttk.Button(self.root, text="Alterar", command=self.alterar).grid(row=3, column=1)
        ttk.Button(self.root, text="Excluir", command=self.excluir).grid(row=4, column=0)
        ttk.Button(self.root, text="Listar", command=self.listar).grid(row=4, column=1)

        self.text_area = tk.Text(self.root, height=10, width=70)
        self.text_area.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def cadastrar(self):
        try:
            nome = self.entries["nome"].get()
            senha = self.entries["senha"].get()
            if not nome or not senha:
                raise ValueError("Preencha todos os campos.")
            self.db.inserir_cliente(nome, senha)
            self.limpar()
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def alterar(self):
        try:
            idcliente = self.entries["id"].get()
            nome = self.entries["nome"].get()
            senha = self.entries["senha"].get()
            if not idcliente or not nome or not senha:
                raise ValueError("Todos os campos devem ser preenchidos.")
            self.db.alterar_cliente(idcliente, nome, senha)
            self.limpar()
            messagebox.showinfo("Sucesso", "Cliente alterado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir(self):
        try:
            idcliente = self.entries["id"].get()
            if not idcliente:
                raise ValueError("Informe o ID do cliente a excluir.")
            self.db.excluir_cliente(idcliente)
            self.limpar()
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def listar(self):
        try:
            clientes = self.db.listar_clientes()
            self.text_area.delete(1.0, tk.END)
            for c in clientes:
                self.text_area.insert(tk.END, f"ID: {c[0]} | Nome: {c[1]} | Senha: {c[2]}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def limpar(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = ClienteADMApp(root)
    root.mainloop()
