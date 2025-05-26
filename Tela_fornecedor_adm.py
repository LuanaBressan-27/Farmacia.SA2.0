# Importação das bibliotecas necessárias
import tkinter as tk  # Interface gráfica
from tkinter import messagebox, Menu  # Caixas de mensagem e menus
from crud_fornecedores import add_supplier, read_suppliers, update_supplier, delete_supplier  # Funções de banco de dados
import subprocess  # Para abrir outro script externo

# Classe principal da interface gráfica para gerenciamento de fornecedores
class FornecedorADMApp:
    def __init__(self, root):
        self.root = root  # Janela principal
        self.root.title("Gestão de Fornecedores - ADM")  # Título da janela
        self.root.geometry("800x600")  # Tamanho da janela
        self.root.configure(background="#e6f2ff")  # Cor de fundo azul claro
        self.root.resizable(width=False, height=False)  # Impede redimensionamento da janela

        self.criar_menu()     # Chama o método para criar o menu superior
        self.criar_widgets()  # Chama o método para criar os campos e botões

    # Método para criar o menu superior com opções de navegação (não estão implementadas ainda)
    def criar_menu(self):
        menu_bar = Menu(self.root)  # Cria a barra de menu
        menu = Menu(menu_bar, tearoff=0)  # Cria o menu suspenso
        menu.add_command(label="Produtos")  # Opção Produtos
        menu.add_command(label="Funcionários")  # Opção Funcionários
        menu.add_command(label="Clientes")  # Opção Clientes
        menu_bar.add_cascade(label="Menu", menu=menu)  # Adiciona o menu suspenso à barra
        self.root.config(menu=menu_bar)  # Aplica o menu à janela principal

    # Método para criar os campos de entrada, botões e área de texto
    def criar_widgets(self):
        # Lista de campos (rótulo mostrado e nome interno do campo)
        campos = [
            ("ID", "id"),
            ("Nome da Empresa", "nome_empresa"),
            ("Email", "email"),
            ("Telefone", "telefone"),
            ("Produto", "produto"),
            ("Transporte", "transporte"),
            ("Início do Contrato", "inicio_contrato"),
            ("Final do Contrato", "final_contrato")
        ]

        self.entries = {}  # Dicionário para armazenar os campos de entrada

        # Cria os rótulos e os campos de entrada
        for i, (label_text, field_name) in enumerate(campos):
            tk.Label(self.root, text=label_text + ":", bg="#e6f2ff").grid(row=i, column=0, sticky="e", padx=10, pady=5)
            entry = tk.Entry(self.root, width=40)  # Cria campo de entrada
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[field_name] = entry  # Salva o campo no dicionário

        # Botões de ação
        tk.Button(self.root, text="Adicionar", command=self.adicionar).grid(row=8, column=0, pady=10)
        tk.Button(self.root, text="Atualizar", command=self.atualizar).grid(row=8, column=1)
        tk.Button(self.root, text="Excluir", command=self.excluir).grid(row=8, column=2)
        tk.Button(self.root, text="Voltar", command=self.retornar).grid(row=8, column=3)
        tk.Button(self.root, text="Listar", command=self.listar).grid(row=9, column=0, columnspan=4, pady=5)

        # Área de texto para mostrar a lista de fornecedores
        self.text_area = tk.Text(self.root, height=15, width=90)
        self.text_area.grid(row=10, column=0, columnspan=4, padx=10, pady=10)

    # Coleta os dados digitados nos campos de entrada
    def coletar_dados(self, sem_id=False):
        dados = {}
        for campo, entry in self.entries.items():
            if sem_id and campo == "id":  # Ignora o ID se solicitado
                continue
            dados[campo] = entry.get()  # Pega o valor digitado
        return dados

    # Limpa todos os campos de entrada
    def limpar(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)  # Apaga o conteúdo do campo

    # Adiciona um novo fornecedor usando a função do CRUD
    def adicionar(self):
        try:
            dados = self.coletar_dados(sem_id=True)  # Coleta todos os campos exceto ID
            add_supplier(**dados)  # Chama função do CRUD para inserir no banco
            self.limpar()  # Limpa os campos
            messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")  # Mensagem de sucesso
        except Exception as e:
            messagebox.showerror("Erro", str(e))  # Mostra erro, se houver

    # Atualiza um fornecedor existente
    def atualizar(self):
        try:
            idf = self.entries["id"].get()
            if not idf:
                raise ValueError("ID obrigatório para atualizar")  # Verifica se ID foi informado
            dados = self.coletar_dados(sem_id=True)  # Coleta os outros campos
            update_supplier(idf, **dados)  # Chama a função de atualização
            self.limpar()
            messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Exclui um fornecedor com base no ID
    def excluir(self):
        try:
            idf = self.entries["id"].get()
            if not idf:
                raise ValueError("ID obrigatório para excluir")  # ID é necessário
            delete_supplier(idf)  # Chama a função de exclusão
            self.limpar()
            messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Lista todos os fornecedores na área de texto
    def listar(self):
        try:
            fornecedores = read_suppliers()  # Pega os dados do banco
            self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
            for f in fornecedores:
                # Insere cada fornecedor no formato desejado
                self.text_area.insert(tk.END,
                    f"ID: {f[0]} | Nome: {f[1]} | Email: {f[2]} | Produto: {f[7]} | Transporte: {f[3]} | "
                    f"Início: {f[4]} | Fim: {f[5]} | Telefone: {f[6]}\n"
                )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Volta para o menu principal (abre outro script)
    def retornar(self):
        self.root.withdraw()  # Oculta a janela atual
        subprocess.Popen(["python", "menu_adm.py"])  # Executa o menu_adm.py

# Código principal para executar a janela
if __name__ == '__main__':
    root = tk.Tk()  # Cria a janela principal do Tkinter
    app = FornecedorADMApp(root)  # Cria uma instância do app
    root.mainloop()  # Inicia o loop da interface
