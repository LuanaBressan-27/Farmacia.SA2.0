import tkinter as tk
from tkinter import ttk, messagebox, Menu
from crud_funcionarios import Database

class FuncionarioADMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestão de Funcionários - ADM")
        self.root.geometry("800x600")
        self.root.configure(background="#e6f2ff")
        self.db = Database()
        self.criar_menu()
        self.criar_widgets()

    def criar_menu(self):
        menu_bar = Menu(self.root)
        menu = Menu(menu_bar, tearoff=0)
        menu.add_command(label="Produtos")
        menu.add_command(label="Fornecedores")
        menu.add_command(label="Clientes")
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

    def criar_widgets(self):
        campos = ["ID", "Nome", "CPF", "Email", "Telefone", "Função", "Qtd Vendas", "Salário", "Início Contrato"]
        self.entries = {}
        for i, campo in enumerate(campos):
            tk.Label(self.root, text=campo + ":", bg="#e6f2ff").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.root, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[campo.lower().replace(" ", "_").replace("ã", "a").replace("ç", "c").replace("í", "i")] = entry

        ttk.Button(self.root, text="Cadastrar", command=self.cadastrar).grid(row=9, column=0, pady=10)
        ttk.Button(self.root, text="Alterar", command=self.alterar).grid(row=9, column=1)
        ttk.Button(self.root, text="Excluir", command=self.excluir).grid(row=9, column=2)
        ttk.Button(self.root, text="Listar", command=self.listar).grid(row=10, column=0, columnspan=3)

        self.text_area = tk.Text(self.root, height=10, width=90)
        self.text_area.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

    def cadastrar(self):
        try:
            dados = self.obter_dados(True)
            self.db.inserir_funcionario(**dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def alterar(self):
        try:
            idfuncionario = self.entries["id"].get()
            if not idfuncionario:
                raise ValueError("ID obrigatório para alterar.")
            dados = self.obter_dados(True)
            self.db.alterar_funcionario(idfuncionario, **dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Funcionário alterado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir(self):
        try:
            idfuncionario = self.entries["id"].get()
            if not idfuncionario:
                raise ValueError("ID obrigatório para excluir.")
            self.db.excluir_funcionario(idfuncionario)
            self.limpar()
            messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def listar(self):
        try:
            lista = self.db.listar_funcionarios()
            self.text_area.delete(1.0, tk.END)
            for f in lista:
                self.text_area.insert(tk.END, f"ID: {f[0]} | Nome: {f[1]} | CPF: {f[2]} | Email: {f[3]} | Telefone: {f[4]} | Função: {f[5]} | Vendas: {f[6]} | Salário: {f[7]} | Início: {f[8]}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def obter_dados(self, excluir_id=False):
        dados = {}
        for k, v in self.entries.items():
            if excluir_id and k == "id":
                continue
            dados[k] = v.get()
        return dados

    def limpar(self):
        for v in self.entries.values():
            v.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = FuncionarioADMApp(root)
    root.mainloop()

