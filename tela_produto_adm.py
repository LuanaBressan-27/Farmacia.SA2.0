import tkinter as tk
from tkinter import messagebox, Menu
from crud_produtos import add_product, read_products, update_product, delete_product

class ProdutoADMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Produtos - ADM")
        self.root.geometry("800x600")
        self.root.configure(background="#e6f2ff")
        self.criar_menu()
        self.criar_widgets()

    def criar_menu(self):
        menu_bar = Menu(self.root)
        menu = Menu(menu_bar, tearoff=0)
        menu.add_command(label="Funcionários")
        menu.add_command(label="Fornecedores")
        menu.add_command(label="Clientes")
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

    def criar_widgets(self):
        labels = [
            "ID", "Nome do Produto", "Tipo", "Quantidade Enviada", "Tempo de Validade",
            "Data de Fabricação", "Lote", "Fornecedor", "Quantidade em Estoque"
        ]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self.root, text=label + ":", bg="#e6f2ff").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.root, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5)
            chave = label.lower().replace(" ", "_").replace("ç", "c")
            self.entries[chave] = entry

        tk.Button(self.root, text="Adicionar", command=self.adicionar).grid(row=9, column=0, pady=10)
        tk.Button(self.root, text="Atualizar", command=self.atualizar).grid(row=9, column=1, pady=10)
        tk.Button(self.root, text="Excluir", command=self.excluir).grid(row=9, column=2, pady=10)
        tk.Button(self.root, text="Listar Produtos", command=self.listar).grid(row=10, column=0, columnspan=3, pady=10)

        self.text_area = tk.Text(self.root, height=15, width=90)
        self.text_area.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

    def adicionar(self):
        try:
            dados = self.obter_dados(sem_id=True)
            add_product(**dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def atualizar(self):
        try:
            id_produto = self.entries["id"].get().strip()
            if not id_produto:
                raise ValueError("ID obrigatório para atualizar.")
            dados = self.obter_dados(sem_id=True)
            update_product(id_produto, **dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir(self):
        try:
            id_produto = self.entries["id"].get().strip()
            if not id_produto:
                raise ValueError("ID obrigatório para exclusão.")
            delete_product(id_produto)
            self.limpar()
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def listar(self):
        try:
            produtos = read_products()
            self.text_area.delete(1.0, tk.END)
            for p in produtos:
                self.text_area.insert(
                    tk.END,
                    f"ID: {p[0]} | Nome: {p[1]} | Tipo: {p[2]} | Quantidade: {p[3]} | Validade: {p[4]} | "
                    f"Fabricação: {p[5]} | Lote: {p[6]} | Fornecedor: {p[7]} | Estoque: {p[8]}\n"
                )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def obter_dados(self, sem_id=False):
        campos = self.entries.copy()
        if sem_id:
            campos.pop("id")
        dados = {}
        for chave, entry in campos.items():
            valor = entry.get().strip()
            if not valor:
                raise ValueError("Todos os campos devem ser preenchidos!")
            dados[chave] = valor
        return dados

    def limpar(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProdutoADMApp(root)
    root.mainloop()
