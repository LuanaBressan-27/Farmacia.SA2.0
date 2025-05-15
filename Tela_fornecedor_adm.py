import tkinter as tk
from tkinter import messagebox, Menu
from crud_fornecedores import add_supplier, read_suppliers, update_supplier, delete_supplier

class FornecedorADMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Fornecedores - ADM")
        self.root.geometry("800x600")
        self.root.configure(background="#e6f2ff")
        root.resizable(width=False, height=False)

        self.criar_menu()
        self.criar_widgets()

    def criar_menu(self):
        menu_bar = Menu(self.root)
        menu = Menu(menu_bar, tearoff=0)
        menu.add_command(label="Produtos")
        menu.add_command(label="Funcionários")
        menu.add_command(label="Clientes")
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

    def criar_widgets(self):
        labels = ["ID", "Nome da Empresa", "Email", "Telefone", "Produto", "Transporte", "Início do Contrato", "Final do Contrato"]
        self.entries = {}

        for i, label in enumerate(labels):
            tk.Label(self.root, text=label + ":", bg="#e6f2ff").grid(row=i, column=0, sticky="e", padx=10, pady=5)
            entry = tk.Entry(self.root, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label.lower().replace(" ", "_").replace("ã", "a").replace("í", "i").replace("ç", "c")] = entry

        tk.Button(self.root, text="Adicionar", command=self.adicionar).grid(row=8, column=0, pady=10)
        tk.Button(self.root, text="Atualizar", command=self.atualizar).grid(row=8, column=1)
        tk.Button(self.root, text="Excluir", command=self.excluir).grid(row=8, column=2)
        tk.Button(self.root, text="Listar", command=self.listar).grid(row=9, column=0, columnspan=3)
        tk.Button(self.root, text="Voltar",command=retornar).grid(row=8,column=3)

        self.text_area = tk.Text(self.root, height=15, width=90)
        self.text_area.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

    def adicionar(self):
        try:
            dados = self.coletar_dados(True)
            add_supplier(**dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def atualizar(self):
        try:
            idf = self.entries["id"].get()
            if not idf:
                raise ValueError("ID obrigatório para atualizar")
            dados = self.coletar_dados(True)
            update_supplier(idf, **dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir(self):
        try:
            idf = self.entries["id"].get()
            if not idf:
                raise ValueError("ID obrigatório para excluir")
            delete_supplier(idf)
            self.limpar()
            messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def listar(self):
        try:
            fornecedores = read_suppliers()
            self.text_area.delete(1.0, tk.END)
            for f in fornecedores:
                self.text_area.insert(tk.END, f"ID: {f[0]} | Empresa: {f[1]} | Email: {f[2]} | Telefone: {f[3]} | Produto: {f[4]} | Transporte: {f[5]} | Início: {f[6]} | Final: {f[7]}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def coletar_dados(self, sem_id=False):
        campos = self.entries.copy()
        if sem_id:
            campos.pop("id")
        return {chave: entry.get() for chave, entry in campos.items()}

    def limpar(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
def retornar():
    root.destroy()
    import menu_adm
if __name__ == '__main__':
    root = tk.Tk()
    app = FornecedorADMApp(root)
    root.mainloop()
