# Importa os módulos necessários do tkinter para a interface gráfica
import tkinter as tk
from tkinter import ttk, messagebox, Menu
from crud_clientes import Database  # Importa a classe de banco de dados personalizada para manipulação de clientes
import subprocess  # Para executar outro script Python (menu_adm.py)

# Classe principal da aplicação de gestão de clientes para administradores
class ClienteADMApp:
    def __init__(self, root):
        self.root = root
        
        # Garante que a janela principal esteja visível
        if root == root.withdraw:  # Este trecho está incorreto (ver nota abaixo)
            root.deiconify
        
        # Configurações básicas da janela
        self.root.title("Gestão de Clientes - ADM")
        self.root.geometry("600x500")
        self.root.configure(background="#e6f2ff")  # Define a cor de fundo azul claro
        root.resizable(width=False, height=False)  # Impede o redimensionamento da janela

        self.db = Database()  # Instancia o objeto de acesso ao banco de dados

        self.criar_menu()     # Cria o menu superior da aplicação
        self.criar_widgets()  # Cria os elementos da interface gráfica (entradas, botões, etc.)

    def criar_menu(self):
        # Cria a barra de menu superior
        menu_bar = Menu(self.root)
        menu = Menu(menu_bar, tearoff=0)  # Menu drop-down sem borda destacável
        menu.add_command(label="Produtos")      # Item do menu (não funcional aqui)
        menu.add_command(label="Funcionários")  # Item do menu (não funcional aqui)
        menu.add_command(label="Fornecedores")  # Item do menu (não funcional aqui)
        menu_bar.add_cascade(label="Menu", menu=menu)  # Adiciona o menu drop-down à barra
        self.root.config(menu=menu_bar)

    def criar_widgets(self):
        # Cria os rótulos e entradas para os campos de ID, Nome e Senha
        labels = ["ID", "Nome de Usuário", "Senha"]
        self.entries = {}  # Dicionário para armazenar os campos de entrada

        for i, label in enumerate(labels):
            tk.Label(self.root, text=label + ":", bg="#e6f2ff").grid(row=i, column=0, padx=10, pady=10, sticky="e")
            entry = tk.Entry(self.root, width=40)
            if "senha" in label.lower():
                entry.config(show="*")  # Oculta os caracteres da senha
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.entries[label.lower().split()[0]] = entry  # Armazena o campo no dicionário com chave 'id', 'nome', ou 'senha'

        # Botões de ação
        ttk.Button(self.root, text="Cadastrar", command=self.cadastrar).grid(row=3, column=0)
        ttk.Button(self.root, text="Alterar", command=self.alterar).grid(row=3, column=2)
        ttk.Button(self.root, text="Excluir", command=self.excluir).grid(row=4, column=0)
        ttk.Button(self.root, text="Listar", command=self.listar).grid(row=4, column=2)
        ttk.Button(self.root, text="Voltar", command=retornar).grid(row=4, column=1)

        # Área de texto para exibir a lista de clientes
        self.text_area = tk.Text(self.root, height=10, width=60)
        self.text_area.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    # Método para cadastrar um novo cliente
    def cadastrar(self):
        try:
            nome = self.entries["nome"].get()
            senha = self.entries["senha"].get()
            if not nome or not senha:
                raise ValueError("Preencha todos os campos.")
            self.db.inserir_cliente(nome, senha)  # Insere no banco de dados
            self.limpar()
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Método para alterar dados de um cliente existente
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

    # Método para excluir um cliente do banco de dados
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

    # Método para listar todos os clientes cadastrados
    def listar(self):
        try:
            clientes = self.db.listar_clientes()
            self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
            for c in clientes:
                self.text_area.insert(tk.END, f"ID: {c[0]} | Nome: {c[1]} | Senha: {c[2]}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Método para limpar todos os campos de entrada
    def limpar(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Função para voltar ao menu principal
def retornar():
    root.withdraw()  # Oculta a janela atual
    subprocess.Popen(["python", "menu_adm.py"])  # Executa o arquivo menu_adm.py em novo processo

# Bloco principal que inicia a aplicação
if __name__ == '__main__':
    root = tk.Tk()              # Cria a janela principal do Tkinter
    app = ClienteADMApp(root)   # Inicializa a aplicação com a janela
    root.mainloop()             # Inicia o loop da interface