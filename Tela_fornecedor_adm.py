import tkinter as tk
from tkinter import messagebox
from crud_stuff_fornecedores import add_supplier, read_suppliers, update_supplier, delete_supplier

class TelaFornecedor:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Fornecedores")
        self.create_widgets()

    def create_widgets(self):
        # Configuração de layout
        input_frame = tk.Frame(self.root)
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, padx=10, pady=10)

        text_frame = tk.Frame(self.root)
        text_frame.grid(row=2, column=0, padx=10, pady=10)

        # Labels e campos de entrada
        labels = ["Nome", "Email", "Produto", "Transporte", "Início do Contrato",
                  "Final do Contrato", "Cidade", "Estado", "ID Fornecedor"]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(input_frame, text=f"{label}:").grid(row=i, column=0, sticky="e", pady=5)
            entry = tk.Entry(input_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            # Correção do nome da chave
            self.entries[label.lower().replace(" ", "_")] = entry

        # Botões
        tk.Button(button_frame, text="Adicionar Fornecedor", command=self.add_supplier).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Atualizar Fornecedor", command=self.update_supplier).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Excluir Fornecedor", command=self.delete_supplier).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Listar Fornecedores", command=self.list_suppliers).grid(row=0, column=3, padx=5)

        # Área de texto para exibir fornecedores
        self.text_area = tk.Text(text_frame, height=10, width=80)
        self.text_area.pack()

    def add_supplier(self):
        values = {key: entry.get().strip() for key, entry in self.entries.items() if key != "id_fornecedor"}
        if all(values.values()):
            try:
                add_supplier(
                    values["nome"], values["email"], values["produto"], values["transporte"],
                    values["início_do_contrato"], values["final_do_contrato"], values["cidade"], values["estado"]
                )
                self.clear_entries()
                messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar fornecedor: {e}")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios para adicionar um fornecedor.")

    def update_supplier(self):
        id_fornecedor = self.entries["id_fornecedor"].get().strip()  # Chave corrigida
        values = {key: entry.get().strip() for key, entry in self.entries.items() if key != "id_fornecedor"}
        if id_fornecedor and all(values.values()):
            try:
                update_supplier(
                    id_fornecedor, values["nome"], values["email"], values["produto"], values["transporte"],
                    values["início_do_contrato"], values["final_do_contrato"], values["cidade"], values["estado"]
                )
                self.clear_entries()
                messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao atualizar fornecedor: {e}")
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios para atualizar um fornecedor.")

    def delete_supplier(self):
        id_fornecedor = self.entries["id_fornecedor"].get().strip()  # Chave corrigida
        if id_fornecedor:
            try:
                delete_supplier(id_fornecedor)
                self.clear_entries()
                messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao excluir fornecedor: {e}")
        else:
            messagebox.showerror("Erro", "ID do fornecedor é obrigatório para excluir.")

    def list_suppliers(self):
        try:
            suppliers = read_suppliers()
            self.text_area.delete(1.0, tk.END)
            for supplier in suppliers:
                self.text_area.insert(
                    tk.END,
                    f"ID: {supplier[0]}, Nome: {supplier[1]}, Email: {supplier[2]}, Produto: {supplier[3]}, "
                    f"Transporte: {supplier[4]}, Início do Contrato: {supplier[5]}, Final do Contrato: {supplier[6]}, "
                    f"Cidade: {supplier[7]}, Estado: {supplier[8]}\n"
                )
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao listar fornecedores: {e}")

    def clear_entries(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaFornecedor(root)
    root.mainloop()
