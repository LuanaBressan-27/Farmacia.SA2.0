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
        self.root.geometry("1000x700")  # Janela maior para comportar área maior
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
        self.text_area = tk.Text(self.root, height=40, width=120)  # Área de texto maior
        self.text_area.pack(padx=10, pady=10)  # Posiciona a área com margem

    # Função que busca e exibe os produtos
    def mostrar_produtos(self):
        try:
            produtos = read_products()
            self.text_area.delete(1.0, tk.END)
            # Cabeçalho formatado
            header = "{:<4} {:<20} {:<10} {:<10} {:<12} {:<12} {:<8} {:<15} {:<8}\n".format(
                "ID", "Nome", "Tipo", "Qtd", "Validade", "Fabricação", "Lote", "Fornecedor", "Estoque"
            )
            self.text_area.insert(tk.END, header)
            self.text_area.insert(tk.END, "-"*110 + "\n")
            for p in produtos:
                linha = "{:<4} {:<20} {:<10} {:<10} {:<12} {:<12} {:<8} {:<15} {:<8}\n".format(
                    p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]
                )
                self.text_area.insert(tk.END, linha)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Função que busca e exibe os fornecedores
    def mostrar_fornecedores(self):
        try:
            fornecedores = read_suppliers()
            self.text_area.delete(1.0, tk.END)
            header = "{:<4} {:<20} {:<25} {:<15} {:<15} {:<12} {:<12} {:<12}\n".format(
                "ID", "Empresa", "Email", "Telefone", "Produto", "Transporte", "Início", "Final"
            )
            self.text_area.insert(tk.END, header)
            self.text_area.insert(tk.END, "-"*120 + "\n")
            for f in fornecedores:
                linha = "{:<4} {:<20} {:<25} {:<15} {:<15} {:<12} {:<12} {:<12}\n".format(
                    f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7]
                )
                self.text_area.insert(tk.END, linha)
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    # Função que busca e exibe os clientes
    def mostrar_clientes(self):
        try:
            db = DBCliente()
            clientes = db.listar_clientes()
            self.text_area.delete(1.0, tk.END)
            header = "{:<4} {:<20} {:<15} {:<30} {:<15} {:<15}\n".format(
                "ID", "Nome", "Senha", "Email", "Telefone", "CPF"
            )
            self.text_area.insert(tk.END, header)
            self.text_area.insert(tk.END, "-"*100 + "\n")
            for c in clientes:
                linha = "{:<4} {:<20} {:<15} {:<30} {:<15} {:<15}\n".format(
                    c[0], c[1], c[2], c[3], c[4], c[5]
                )
                self.text_area.insert(tk.END, linha)
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
