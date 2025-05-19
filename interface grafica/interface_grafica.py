import tkinter as tk

janela = tk.Tk()
janela.title("Aula de RAD em Python")
janela.geometry("400x300")

label = tk.Label(text="Aula de RAD em Python", font=("Arial", 14), fg="blue")
label.pack(pady=20)
janela.mainloop()


def acao_botao():
    print("Botão pressionado!")


botao = tk.Button(text="Clique aqui", command=acao_botao, bg="green", fg="white")
botao.pack()

entrada = tk.Entry(width=30)
entrada.pack()

opcao = tk.StringVar(value="Python")

tk.Radiobutton(
    text="Aula de Python boa", variable=opcao, value="Aula de Python boa"
).pack()

tk.Radiobutton(
    text="Aula de Python MUITO boa", variable=opcao, value="Aula de Python MUITO boa"
).pack()

check_var = tk.BooleanVar()

check = tk.Checkbutton(
    text="Aceito os termos", variable=check_var, onvalue=True, offvalue=False
)
check.pack()

# Verificar Estado
print(check_var.get())

janela.mainloop()

texto = tk.Text(height=5, width=30)
texto.pack()

# Inserir conteúdo:
texto.insert("1.0", "que aula boa...")

# Obter o conteúdo:
conteudo = texto.get("1.0", "end")

janela.mainloop()

msg = tk.Message(
    text="Esta mensagem se ajusta automaticamente ao tamanho da janela", width=150
)

msg.pack()


def mostrar_valor(val):
    print(f"Valor: {val}")


slider = tk.Scale(from_=0, to=100, orient="horizontal", command=mostrar_valor)
slider.pack()

janela.mainloop()


from tkinter import messagebox

# Mostrar mensagem
messagebox.showinfo("Título", "Operação Concluída!")

# Pergunta Sim/Não
resposta = messagebox.askyesno("Confirmação", "Deseja continuar")
print(resposta)

janela.mainloop()
