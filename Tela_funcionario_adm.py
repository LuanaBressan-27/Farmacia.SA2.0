# Importações necessárias para a interface e banco
import tkinter as tk  # Biblioteca para criar interfaces gráficas
from tkinter import ttk, messagebox, Menu  # Widgets adicionais e janelas de aviso
from crud_funcionarios import Database  # Módulo com a classe de conexão e operações no banco
import subprocess  # Para abrir outro script

# Classe principal da aplicação para gerenciamento de funcionários (nível ADM)
class FuncionarioADMApp:
    def __init__(self, root):
        self.root = root

        # (Tentativa desnecessária de verificação - esse bloco abaixo pode ser removido)
        if root == root.withdraw:
            root.deiconify  # Isto não executa nada porque falta parênteses

        # Configuração da janela principal
        self.root.title("Gestão de Funcionários - ADM")
        self.root.geometry("800x600")  # Tamanho da janela
        self.root.configure(background="#e6f2ff")  # Cor de fundo azul claro
        root.resizable(width=False, height=False)  # Impede redimensionamento

        self.db = Database()  # Instancia o objeto de banco de dados

        self.criar_menu()      # Cria o menu superior
        self.criar_widgets()   # Cria os campos e botões

    # Cria a barra de menu da aplicação
    def criar_menu(self):
        menu_bar = Menu(self.root)  # Barra de menu
        menu = Menu(menu_bar, tearoff=0)  # Menu suspenso

        # Opções do menu (não estão ligadas a nenhuma ação ainda)
        menu.add_command(label="Produtos")
        menu.add_command(label="Fornecedores")
        menu.add_command(label="Clientes")

        menu_bar.add_cascade(label="Menu", menu=menu)  # Adiciona o menu suspenso à barra
        self.root.config(menu=menu_bar)  # Aplica o menu na janela principal

    # Cria os campos de entrada, botões e área de texto
    def criar_widgets(self):
        # Lista com os nomes dos campos a serem exibidos
        campos = ["ID", "Nome", "CPF", "Email", "Telefone", "Função", "Qtd Vendas", "Salario", "Início_Contrato"]
        self.entries = {}  # Dicionário para armazenar os campos de entrada

        # Cria os rótulos e campos de entrada para cada item
        for i, campo in enumerate(campos):
            tk.Label(self.root, text=campo + ":", bg="#e6f2ff").grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.root, width=40)  # Campo de texto
            entry.grid(row=i, column=1, padx=10, pady=5)

            # Converte o nome para chave válida (sem espaços e acentos)
            chave = campo.lower().replace(" ", "_").replace("ã", "a").replace("ç", "c").replace("í", "i")
            self.entries[chave] = entry

        # Botões de ação com comandos associados
        ttk.Button(self.root, text="Cadastrar", command=self.cadastrar).grid(row=9, column=0, pady=10)
        ttk.Button(self.root, text="Alterar", command=self.alterar).grid(row=9, column=1)
        ttk.Button(self.root, text="Excluir", command=self.excluir).grid(row=9, column=2)
        ttk.Button(self.root, text="Listar", command=self.listar).grid(row=10, column=0, columnspan=3)
        ttk.Button(self.root, text="Voltar", command=retornar).grid(row=10, column=0)

        # Área de texto para exibir os dados listados
        self.text_area = tk.Text(self.root, height=10, width=60)
        self.text_area.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

    # Cadastra novo funcionário
    def cadastrar(self):
        try:
            dados = self.obter_dados(True)  # Coleta os dados, exceto ID
            self.db.inserir_funcionario(**dados)  # Insere no banco de dados
            self.limpar()  # Limpa os campos
            messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso!")  # Mensagem de sucesso
        except Exception as e:
            messagebox.showerror("Erro", str(e))  # Exibe erro se ocorrer

    # Altera dados de um funcionário existente
    def alterar(self):
        try:
            idfuncionario = self.entries["id"].get()
            if not idfuncionario:
                raise ValueError("ID obrigatório para alterar.")
            dados = self.obter_dados(True)  # Coleta os dados (sem o ID novamente)
            self.db.alterar_funcionario(idfuncionario, **dados)
            self.limpar()
            messagebox.showinfo("Sucesso", "Funcionário alterado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Exclui um funcionário pelo ID
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

    # Lista todos os funcionários cadastrados
    def listar(self):
        try:
            lista = self.db.listar_funcionarios()
            self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
            for f in lista:
                # Formata e exibe cada funcionário na tela
                self.text_area.insert(
                    tk.END,
                    f"ID: {f[0]} | Nome: {f[1]} | CPF: {f[2]} | Email: {f[3]} | "
                    f"Telefone: {f[4]} | Função: {f[5]} | Vendas: {f[6]} | "
                    f"Salario: {f[7]} | Início: {f[8]}\n"
                )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Coleta os dados digitados nos campos (com ou sem ID)
    def obter_dados(self, excluir_id=False):
        dados = {}
        for k, v in self.entries.items():
            if excluir_id and k == "id":
                continue
            dados[k] = v.get()
        return dados

    # Limpa todos os campos de entrada
    def limpar(self):
        for v in self.entries.values():
            v.delete(0, tk.END)

# Função chamada pelo botão "Voltar" que oculta a tela atual e abre menu_adm.py
def retornar():
    root.withdraw()
    subprocess.Popen(["python", "menu_adm.py"])

# Código principal que executa o aplicativo
if __name__ == '__main__':
    root = tk.Tk()  # Cria a janela principal
    app = FuncionarioADMApp(root)  # Instancia a aplicação
    root.mainloop()  # Inicia o loop da interface
