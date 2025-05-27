# Importa os módulos necessários
import tkinter as tk
from tkinter import ttk, messagebox, Menu
from crud_clientes import Database  # Classe personalizada de banco de dados
import subprocess  # Permite abrir outro script Python

# Classe principal da aplicação de administração de clientes
class ClienteADMApp:
    def __init__(self, root):
        self.root = root

        # Configurações da janela principal
        self.root.title("Gestão de Clientes - ADM")
        self.root.geometry("600x550")
        self.root.configure(background="#e6f2ff")
        root.resizable(width=False, height=False)

        # Instancia o banco de dados
        self.db = Database()

        # Inicializa menu e interface gráfica
        self.criar_menu()
        self.criar_widgets()

    def criar_widgets(self):
        # Lista de campos que o formulário irá ter
        labels = ["ID", "Nome", "Senha", "email", "telefone", "CPF"]
        self.entries = {}  # Dicionário para armazenar os campos de entrada

        # Cria rótulos e campos de entrada para cada item
        for i, label in enumerate(labels):
            tk.Label(self.root, text=label + ":", bg="#e6f2ff").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.root, width=40)
            if "senha" in label.lower():
                entry.config(show="*")  # Oculta caracteres se for senha
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label.lower()] = entry  # Armazena o campo com chave em minúsculo

        # Botões de ação
        ttk.Button(self.root, text="Cadastrar", command=self.cadastrar).grid(row=6, column=0, pady=10)
        ttk.Button(self.root, text="Alterar", command=self.alterar).grid(row=6, column=2, pady=10)
        ttk.Button(self.root, text="Excluir", command=self.excluir).grid(row=7, column=0)
        ttk.Button(self.root, text="Listar", command=self.listar).grid(row=7, column=2)
        ttk.Button(self.root, text="Voltar", command=retornar).grid(row=7, column=1)

        # Área de texto para exibição dos clientes cadastrados
        self.text_area = tk.Text(self.root, height=10, width=60)
        self.text_area.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    # Função para cadastrar cliente no banco
    def cadastrar(self):
        try:
            # Coleta os dados do formulário (exceto ID)
            dados = {k: e.get() for k, e in self.entries.items() if k != "id"}
            if not all(dados.values()):
                raise ValueError("Preencha todos os campos.")
            # Insere no banco de dados
            self.db.inserir_cliente(**dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Função para alterar um cliente já existente
    def alterar(self):
        try:
            idcliente = self.entries["id"].get()
            dados = {k: e.get() for k, e in self.entries.items() if k != "id"}
            if not idcliente or not all(dados.values()):
                raise ValueError("Todos os campos devem ser preenchidos.")
            self.db.alterar_cliente(idcliente, **dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Cliente alterado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Função para excluir um cliente pelo ID
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

    # Função para listar todos os clientes cadastrados
    def listar(self):
        try:
            clientes = self.db.listar_clientes()
            self.text_area.delete(1.0, tk.END)  # Limpa o campo de texto
            for c in clientes:
                self.text_area.insert(
                    tk.END,
                    f"ID: {c[0]} | Nome: {c[1]} | Senha: {c[2]} | Email: {c[3]} | Telefone: {c[4]} | CPF: {c[5]}\n"
                )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Função auxiliar para limpar os campos de entrada
    def limpar(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Função chamada pelo botão "Voltar"
def retornar():
    root.withdraw()  # Oculta a janela atual
    subprocess.Popen(["python", "menu_adm.py"])  # Abre o menu principal

# Ponto de entrada da aplicação
if __name__ == '__main__':
    root = tk.Tk()
    app = ClienteADMApp(root)
    root.mainloop()
