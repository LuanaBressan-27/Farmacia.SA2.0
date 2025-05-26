# Importa os módulos necessários do tkinter para criar a interface gráfica
import tkinter as tk
from tkinter import Menu, messagebox
from crud_produtos import read_products  # Função para ler produtos do banco de dados
import subprocess  # Para executar outro script externo

# Classe principal da interface restrita para clientes
class ClienteRestritoApp:
    def __init__(self, root):
        self.root = root

        # Tentativa incorreta de verificação para exibir a janela (essa linha não tem efeito prático)
        if root == root.withdraw:
            root.deiconify

        # Configurações básicas da janela
        self.root.title("Acesso Cliente - Produtos Disponíveis")
        self.root.geometry("800x600")  # Define tamanho da janela
        self.root.configure(background="#e6f2ff")  # Define cor de fundo azul claro
        root.resizable(width=False, height=False)  # Desativa redimensionamento

        # Criação dos elementos de interface
        self.criar_menu()
        self.criar_widgets()

    # Método que cria a barra de menu
    def criar_menu(self):
        menu_bar = Menu(self.root)
        menu = Menu(menu_bar, tearoff=0)  # Cria um menu drop-down
        menu.add_command(label="Ver Produtos", command=self.mostrar_produtos)  # Opção para listar produtos
        menu_bar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menu_bar)

    # Método que cria os widgets (elementos visuais) principais da janela
    def criar_widgets(self):
        # Área de texto onde os produtos serão listados
        self.text_area = tk.Text(self.root, height=30, width=100)
        self.text_area.pack(padx=10, pady=10)

        # Botão para voltar ao menu anterior
        tk.Button(root, text="Voltar", command=retornar).pack(padx=10)

    # Método para buscar e exibir os produtos disponíveis
    def mostrar_produtos(self):
        try:
            produtos = read_products()  # Chama função que retorna lista de produtos
            self.text_area.delete(1.0, tk.END)  # Limpa a área de texto

            # Exibe os produtos formatados na área de texto
            for p in produtos:
                self.text_area.insert(
                    tk.END,
                    f"ID: {p[0]} | Nome: {p[1]} | Tipo: {p[2]} | Quantidade: {p[3]} | "
                    f"Validade: {p[4]} | Fabricação: {p[5]} | Lote: {p[6]} | "
                    f"Fornecedor: {p[7]} | Estoque: {p[8]}\n"
                )
        except Exception as e:
            # Exibe mensagem de erro caso algo dê errado
            messagebox.showerror("Erro", str(e))

# Função chamada ao clicar no botão "Voltar"
def retornar():
    root.withdraw()  # Oculta a janela atual
    subprocess.Popen(["python", "menu_cliente.py"])  # Executa o menu do cliente em outro processo

# Bloco principal que inicia a aplicação
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = ClienteRestritoApp(root)  # Inicializa a interface
    root.mainloop()  # Inicia o loop da interface gráfica
