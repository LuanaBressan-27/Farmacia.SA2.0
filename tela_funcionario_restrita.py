# Importações necessárias
import tkinter as tk  # Interface gráfica
from tkinter import Menu, messagebox  # Menu superior e janelas de alerta
from crud_funcionarios import Database as DBFunc  # (Não usado no código atual)
from crud_clientes import Database as DBCliente  # Classe de acesso ao banco de clientes
from crud_produtos import read_products  # Função para listar produtos
from crud_fornecedores import read_suppliers  # Função para listar fornecedores
import subprocess  # Permite abrir outro script

# Classe da interface para o funcionário com acesso restrito (somente leitura)
class FuncionarioRestritoApp:
    def __init__(self, root):
        self.root = root

        # Verificação inútil (pode ser removida)
        if root == root.withdraw:
            root.deiconify  # Não executa porque está sem parênteses

        # Configurações da janela
        self.root.title("Acesso Funcionário - Consulta")
        self.root.geometry("800x600")
        self.root.configure(background="#e6f2ff")  # Cor de fundo azul clara
        root.resizable(width=False, height=False)  # Janela fixa (sem redimensionar)

        self.criar_menu()      # Cria o menu superior
        self.criar_widgets()   # Cria a área de exibição

        # Botão "Voltar" que chama função para retornar ao menu anterior
        tk.Button(root, text="Voltar", command=retornar).pack(pady=10)

    # Criação do menu com opções de consulta
    def criar_menu(self):
        menu_bar = Menu(self.root)  # Barra de menu
        menu = Menu(menu_bar, tearoff=0)  # Menu suspenso

        # Adiciona opções ao menu, com comandos específicos
        menu.add_command(label="Produtos", command=self.mostrar_produtos)
        menu.add_command(label="Fornecedores", command=self.mostrar_fornecedores)
        menu.add_command(label="Clientes", command=self.mostrar_clientes)

        menu_bar.add_cascade(label="Menu", menu=menu)  # Adiciona o menu suspenso à barra
        self.root.config(menu=menu_bar)  # Aplica o menu na janela

    # Cria a área de exibição de dados
    def criar_widgets(self):
        self.text_area = tk.Text(self.root, height=30, width=100)  # Área de texto para exibição
        self.text_area.pack(padx=10, pady=10)  # Posiciona a área com margem

    # Função que busca e exibe os produtos
    def mostrar_produtos(self):
        try:
            produtos = read_products()  # Lê produtos do banco ou arquivo
            self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
            for p in produtos:
                # Formata e insere cada produto na área de exibição
                self.text_area.insert(
                    tk.END,
                    f"ID: {p[0]} | Nome: {p[1]} | Tipo: {p[2]} | Quantidade: {p[3]} | "
                    f"Validade: {p[4]} | Fabricação: {p[5]} | Lote: {p[6]} | "
                    f"Fornecedor: {p[7]} | Estoque: {p[8]}\n"
                )
        except Exception as e:
            messagebox.showerror("Erro", str(e))  # Mostra erro se falhar

    # Função que busca e exibe os fornecedores
    def mostrar_fornecedores(self):
        try:
            fornecedores = read_suppliers()  # Lê dados dos fornecedores
            self.text_area.delete(1.0, tk.END)  # Limpa a área de exibição
            for f in fornecedores:
                self.text_area.insert(
                    tk.END,
                    f"ID: {f[0]} | Empresa: {f[1]} | Email: {f[2]} | Telefone: {f[3]} | "
                    f"Produto: {f[4]} | Transporte: {f[5]} | Início: {f[6]} | Final: {f[7]}\n"
                )
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Função que busca e exibe os clientes
    def mostrar_clientes(self):
        try:
            db = DBCliente()  # Instancia conexão com banco de clientes
            clientes = db.listar_clientes()  # Lista os clientes
            self.text_area.delete(1.0, tk.END)
            for c in clientes:
                self.text_area.insert(tk.END, f"ID: {c[0]} | Nome: {c[1]}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

# Função usada pelo botão "Voltar" para retornar ao menu principal do funcionário
def retornar():
    root.withdraw()  # Oculta a janela atual
    subprocess.Popen(["python", "menu_funcionario.py"])  # Abre o menu do funcionário

# Ponto de entrada do programa
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = FuncionarioRestritoApp(root)  # Inicia o aplicativo
    root.mainloop()  # Mantém a janela aberta
