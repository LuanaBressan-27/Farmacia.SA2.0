from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud_stuff_funcionario import Database

# Tela principal
jan = Tk()
jan.title("Funcionários - Login e Cadastro")
jan.geometry("600x500")
jan.configure(background="lightblue")
jan.resizable(width=False, height=False)

# Título
Titulo = Label(jan, text="Gestão de Funcionários", font=("Century Gothic", 20), bg="darkblue", fg="white")
Titulo.place(x=150, y=10)

# Campos de entrada
labels_text = ["Nome", "Email", "Telefone", "Cidade", "Estado", "Bairro"]
entries = {}

for i, text in enumerate(labels_text):
    label = Label(jan, text=f"{text}:", font=("Century Gothic", 10), bg="lightblue")
    label.place(x=50, y=60 + i * 40)
    entry = ttk.Entry(jan, width=40)
    entry.place(x=150, y=60 + i * 40)
    entries[text.lower()] = entry

# Função de login
def login():
    nome = entries["nome"].get()
    email = entries["email"].get()
    telefone = entries["telefone"].get()
    cidade = entries["cidade"].get()
    estado = entries["estado"].get()
    bairro = entries["bairro"].get()

    if nome == "" or email == "" or telefone == "" or cidade == "" or estado == "" or bairro == "":
        messagebox.showwarning(title="Aviso", message="Por favor, preencha todos os campos!")
        return

    try:
        db = Database()
        resultado = db.verificar_funcionario(nome, email, telefone, cidade, estado, bairro)
        if resultado:
            messagebox.showinfo(title="Login Sucesso", message="Funcionário encontrado no sistema!")
        else:
            messagebox.showwarning(title="Login Falhou", message="Funcionário não cadastrado.")
    except Exception as e:
        messagebox.showerror(title="Erro", message=f"Ocorreu um erro: {e}")

# Funções de cadastro
def exibir_campos_cadastro():
    cadastrar_button.place_forget()

    # Adicionando novos campos
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

    cadastrar_novo_button = ttk.Button(jan, text="Cadastrar", width=20, command=cadastrar_funcionario)
    cadastrar_novo_button.place(x=150, y=430)

    def voltar():
        data_nascimento_label.place_forget()
        data_nascimento_entry.place_forget()
        data_contrato_label.place_forget()
        data_contrato_entry.place_forget()
        cadastrar_novo_button.place_forget()
        voltar_button.place_forget()
        cadastrar_button.place(x=150, y=430)

    voltar_button = ttk.Button(jan, text="Voltar", width=20, command=voltar)
    voltar_button.place(x=300, y=430)

# Botão principal de Cadastrar
cadastrar_button = ttk.Button(jan, text="Cadastrar", width=20, command=exibir_campos_cadastro)
cadastrar_button.place(x=150, y=430)

# Botão de Login
botao_login = ttk.Button(jan, text="Login", width=20, command=login)
botao_login.place(x=300, y=430)

jan.mainloop()
