import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
from models.Aluno import Aluno


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Acadêmico")
        self.root.geometry("800x600")

        # Configuração do DB
        self.db = Database()
        self.db.conectar()
        self.aluno = Aluno(self.db)

        # Widgets
        self.criar_widgets()
        self.atualizar_tabela()

    def criar_widgets(self):
        # Frame de formulário
        form_frame = ttk.Frame(self.root)
        form_frame.pack(pady=10)

        # Entradas
        ttk.Label(form_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.nome = ttk.Entry(form_frame, width=30)
        self.nome.grid(row=0, column=1)

        # [...] Adicione matricula, curso, nota (similar)

        # Botões
        botoes_frame = ttk.Frame(self.root)
        botoes_frame.pack(pady=10)

        # Tabela
        self.tabela = ttk.Treeview(
            self.root,
            column=("ID", "Nome", "Matrícula", "Curso", "Nota"),
            show="headings",
        )
        self.tabela.pack(fill=tk.BOTH, expand=True)

        # Configurar colunas
        for col in self.tabela["columns"]:
            self.tabela.heading(col, text=col)
            self.tabela.column(col, width=100)

        # Bind de seleção
        self.tabela.bind("<<TreeviewSelect>>", self.carregar_selecionado)

    def atualizar_tabela(self):
        # Limpa tabela
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        # Preenche com novos dados
        for aluno in self.aluno.ler_todos():
            self.tabela.insert("", tk.END, values=aluno)

    def salvar(self):
        # Implementar lógica de criação/atualização
        pass

    def editar(self):
        # Implementar edição
        pass

    def carregar_selecionado(self, event):
        # Implementar carregamento dos dados selecionados nos campos
        pass


# Inicialização
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
