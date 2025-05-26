# Importações necessárias para GUI e manipulação de dados
import tkinter as tk
from tkinter import messagebox, Menu
from crud_produtos import add_product, read_products, update_product, delete_product  # Funções do CRUD de produtos
import subprocess  # Para chamar outro script Python

# Classe principal da aplicação para administrador de produtos
class ProdutoADMApp:
    def __init__(self, root):
        self.root = root

        # Essa verificação não faz sentido e pode ser removida
        if root == root.withdraw:
            root.deiconify  # Não executa nada, está mal usada

        # Configurações da janela principal
        self.root.title("Gestão de Produtos - ADM")
        self.root.geometry("800x600")  # Tamanho da janela
        self.root.configure(background="#e6f2ff")  # Cor de fundo azul clara
        root.resizable(width=False, height=False)  # Impede redimensionamento

        self.criar_menu()      # Cria o menu superior
        self.criar_widgets()   # Cria os campos e botões

    # Criação do menu superior com opções
    def criar_menu(self):
        menu_bar = Menu(self.root)
        menu = Menu(menu_bar, tearoff=0)
        menu.add_command(label="Funcionários")     # Navegação fictícia
        menu.add_command(label="Fornecedores")
        menu.add_command(label="Clientes")
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

    # Criação dos widgets (campos de entrada, botões e área de texto)
    def criar_widgets(self):
        # Labels dos campos a serem exibidos
        labels = [
            "ID", "Nome_Produto", "Tipo", "Quantidade Enviada", "Tempo de Validade",
            "Data de Fabricaçao", "Lote", "Fornecedor", "Quantidade em Estoque"
        ]
        self.entries = {}  # Dicionário que armazena os campos de entrada

        # Cria campos de entrada (labels + entry) dinamicamente
        for i, label in enumerate(labels):
            tk.Label(self.root, text=label + ":", bg="#e6f2ff").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.root, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5)
            # Transforma o label em chave: substitui espaços e ç por _
            chave = label.lower().replace(" ", "_").replace("ç", "c")
            self.entries[chave] = entry

        # Botões de ação
        tk.Button(self.root, text="Adicionar", command=self.adicionar).grid(row=9, column=0, pady=10)
        tk.Button(self.root, text="Atualizar", command=self.atualizar).grid(row=9, column=1, pady=10)
        tk.Button(self.root, text="Excluir", command=self.excluir).grid(row=9, column=2, pady=10)
        tk.Button(self.root, text="Listar Produtos", command=self.listar).grid(row=10, column=0, columnspan=3, pady=10)
        tk.Button(root, text="Voltar", command=retornar).grid(row=10, column=0)  # Botão para retornar ao menu anterior

        # Área de texto onde os produtos serão listados
        self.text_area = tk.Text(self.root, height=15, width=90)
        self.text_area.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

    # Adiciona um produto usando o CRUD
    def adicionar(self):
        try:
            dados = self.obter_dados(sem_id=True)  # Não precisa de ID para adicionar
            add_product(**dados)  # Chama função do CRUD para inserir
            self.limpar()
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Atualiza um produto existente
    def atualizar(self):
        try:
            id_produto = self.entries["id"].get().strip()
            if not id_produto:
                raise ValueError("ID obrigatório para atualizar.")
            dados = self.obter_dados(sem_id=True)  # Usa os outros dados, exceto ID
            update_product(id_produto, **dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Exclui um produto a partir do ID
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

    # Lista todos os produtos cadastrados
    def listar(self):
        try:
            produtos = read_products()  # Recupera produtos
            self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
            for p in produtos:
                # Exibe os dados formatados
                self.text_area.insert(
                    tk.END,
                    f"ID: {p[0]} | Nome: {p[1]} | Tipo: {p[2]} | Quantidade: {p[3]} | Validade: {p[4]} | "
                    f"Fabricação: {p[5]} | Lote: {p[6]} | Fornecedor: {p[7]} | Estoque: {p[8]}\n"
                )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Coleta os dados digitados nos campos
    def obter_dados(self, sem_id=False):
        campos = self.entries.copy()
        if sem_id:
            campos.pop("id")  # Remove o campo "id" se não for necessário
        dados = {}
        for chave, entry in campos.items():
            valor = entry.get().strip()
            if not valor:
                raise ValueError("Todos os campos devem ser preenchidos!")
            dados[chave] = valor
        return dados

    # Limpa os campos de entrada
    def limpar(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

# Função usada pelo botão "Voltar"
def retornar():
    root.withdraw()  # Oculta a janela atual
    subprocess.Popen(["python", "menu_adm.py"])  # Abre o menu principal do ADM

# Ponto de entrada da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = ProdutoADMApp(root)  # Instancia o app
    root.mainloop()  # Inicia o loop da interface
