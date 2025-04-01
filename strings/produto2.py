produto = "Caneta"
preco = 2.5
quantidade = 10

recibo = """
produto: {0}
preço unitário: R${1:.2f}
quantidade: {2}
total: R${3:.2f}
""".format(
    produto, preco, quantidade, preco * quantidade
)
print(recibo)
