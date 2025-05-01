import tkinter as tk
from tkinter import ttk
import sqlite3


class Aplicativo:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Alunos")

        # frame principal
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.label_nome = ttk.Label(self.frame, text="Nome:")
        self.entry_nome = ttk.Entry(self.frame, width=30)

        self.label_nota = ttk.Label(self.frame, text="Nota:")
        self.entry_nota = ttk.Entry(self.frame, width=10)

        self.btn_salvar = ttk.Button(
            self.frame, text="Salvar", command=self.salvar_dados
        )

        # Tabela (Treeview)
        self.tabela = ttk.Treeview(
            self.frame, columns=("Nome", "Nota"), show="headings"
        )
        self.tabela.heading("Nome", text="Nome")
        self.tabela.heading("Nota", text="Nota")

        # Layout (grid)
        self.label_nome.grid(row=0, column=0, sticky="w")
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_nota.grid(row=1, column=0, sticky="w")
        self.entry_nota.grid(row=1, column=1, padx=5, pady=5)

        self.btn_salvar.grid(row=2, columnspan=2, pady=10)
        self.tabela.grid(row=3, columnspan=2)

    def salvar_dados(self):
        pass  # Implementaremos depois


# Inicialização
root = tk.Tk()
app = Aplicativo(root)
root.mainloop()
