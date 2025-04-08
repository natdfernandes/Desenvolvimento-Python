# Importar bibliotecas
import pandas as pd

# Extrai os dados da tabela a partir do link da Web
tabelas = pd.read_html(
    "https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria"
)
# Lista com as tabelas
tabelas
