from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud_stuff_funcionario import Database

# Tela principal
jan = Tk()
jan.title("Funcionários ADM - Gestão Completa")
jan.geometry("600x600")
jan.configure(background="lightblue")
jan.resizable(width=False, height=False)

# Título
Titulo = Label(jan, text="Gestão de Funcionários ADM", font=("Century Gothic", 20), bg="darkblue", fg="white")
Titulo.place(x=150, y=10)

# Campos de entrada
labels_text = ["ID", "Nome", "Email", "Telefone", "Cidade", "Estado", "Bairro"]
entries = {}

for i, text in enumerate(labels_text):
    label = Label(jan, text=f"{text}:", font=("Century Gothic", 10), bg="lightblue")
    label.place(x=50, y=60 + i * 40)
    entry = ttk.Entry(jan, width=40)
    entry.place(x=150, y=60 + i * 40)
    entries[text.lower()] = entry

# Campos de Data de Nascimento e Contrato
data_nascimento_label = Label(jan, text="Data de Nascimento:", font=("Century Gothic", 10), bg="lightblue")
data_nascimento_label.place(x=50, y=340)
data_nascimento_entry = ttk.Entry(jan, width=40)
data_nascimento_entry.place(x=200, y=340)
entries["data_de_nascimento"] = data_nascimento_entry

data_contrato_label = Label(jan, text="Data de Contrato:", font=("Century Gothic", 10), bg="lightblue")
data_contrato_label.place(x=50, y=380)
data_contrato_entry = ttk.Entry(jan, width=40)
data_contrato_entry.place(x=200, y=380)
entries["data_de_contrato"] = data_contrato_entry

# Função para cadastrar funcionário
def cadastrar_funcionario():
    nome = entries["nome"].get()
    email = entries["email"].get()
    telefone = entries["telefone"].get()
    cidade = entries["cidade"].get()
    estado = entries["estado"].get()
    bairro = entries["bairro"].get()
    data_nascimento = entries["data_de_nascimento"].get()
    data_contrato = entries["data_de_contrato"].get()

    if nome == "" or email == "" or telefone == "" or cidade == "" or estado == "" or bairro == "" or data_nascimento == "" or data_contrato == "":
        messagebox.showwarning(title="Aviso", message="Por favor, preencha todos os campos!")
        return

    try:
        db = Database()
        db.inserir_funcionario(nome, email, telefone, cidade, estado, bairro, data_nascimento, data_contrato)
        messagebox.showinfo(title="Cadastro Sucesso", message="Funcionário cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror(title="Erro", message=f"Ocorreu um erro: {e}")

# Função para alterar funcionário
def alterar_funcionario():
    id_funcionario = entries["id"].get()
    nome = entries["nome"].get()
    email = entries["email"].get()
    telefone = entries["telefone"].get()
    cidade = entries["cidade"].get()
    estado = entries["estado"].get()
    bairro = entries["bairro"].get()
    data_nascimento = entries["data_de_nascimento"].get()
    data_contrato = entries["data_de_contrato"].get()

    if id_funcionario == "" or nome == "" or email == "" or telefone == "" or cidade == "" or estado == "" or bairro == "" or data_nascimento == "" or data_contrato == "":
        messagebox.showwarning(title="Aviso", message="Por favor, preencha todos os campos!")
        return

    try:
        db = Database()
        db.alterar_funcionario(id_funcionario, nome, email, telefone, cidade, estado, bairro, data_nascimento, data_contrato)
        messagebox.showinfo(title="Alteração Sucesso", message="Funcionário alterado com sucesso!")
    except Exception as e:
        messagebox.showerror(title="Erro", message=f"Ocorreu um erro: {e}")

# Função para excluir funcionário
def excluir_funcionario():
    id_funcionario = entries["id"].get()

    if id_funcionario == "":
        messagebox.showwarning(title="Aviso", message="Por favor, insira o ID do funcionário a ser excluído!")
        return

    try:
        db = Database()
        db.excluir_funcionario(id_funcionario)
        messagebox.showinfo(title="Exclusão Sucesso", message="Funcionário excluído com sucesso!")
    except Exception as e:
        messagebox.showerror(title="Erro", message=f"Ocorreu um erro: {e}")

# Botões principais
cadastrar_button = ttk.Button(jan, text="Cadastrar", width=20, command=cadastrar_funcionario)
cadastrar_button.place(x=50, y=450)

alterar_button = ttk.Button(jan, text="Alterar", width=20, command=alterar_funcionario)
alterar_button.place(x=200, y=450)

excluir_button = ttk.Button(jan, text="Excluir", width=20, command=excluir_funcionario)
excluir_button.place(x=350, y=450)

jan.mainloop()
