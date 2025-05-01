# Importar bibliotecas
import pandas as pd

# Extrai os dados da tabela a partir do link da Web
tabelas = pd.read_html(
    "https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria"
)
# Lista com as tabelas
# print(tabelas)

# Pegando a primeira tabela da lista
tabela = tabelas[0]
# Visualizando tabela
# print(tabela)

# Filtro a tabela com as colunas que quero
tabela_filtrada = tabela[["Diretor(a)", "Bilheteria (US$)"]]
# print(tabela_filtrada)
# Trato os meus dados e transforma em valores numéricos
tabela_filtrada["Bilheteria (US$)"] = (
    tabela_filtrada["Bilheteria (US$)"]
    .str.replace(" ", "")
    .str.replace(".", "")
    .astype("int64")
)
# Faço o agrupamento por diretor
print(tabela_filtrada.groupby("Diretor(a)").sum())
