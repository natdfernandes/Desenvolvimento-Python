import pandas as pd


def ler_csv(ano: int, planilha: str):
    dados = pd.read_csv("./dados/{0}/{1}.csv".format(ano, planilha))
    print("Exibindo dados da planilha {0} de {1}:".format(planilha, ano))
    print(dados)


candidatoPorGenero = "candidatoPorGenero"
candidatoPorIdade = "candidatoPorIdade"
candidatoPorTipoDoador = "candidatoPorTipoDoador"
candidatosPorTipoDoacao = "candidatosPorTipoDoacao"
inaptidaoPorCausas = "inaptidaoPorCausas"
planilhas = [
    candidatoPorGenero,
    candidatoPorIdade,
    candidatoPorTipoDoador,
    candidatosPorTipoDoacao,
    inaptidaoPorCausas,
]

for planilha in planilhas:
    ler_csv(2023, planilha)
    ler_csv(2024, planilha)


dados = pd.read_csv("./dados/{0}/{1}.csv".format(2023, candidatoPorGenero))

print("Exibindo uma coluna da planilha {0}".format(candidatoPorGenero))
print(dados["Aptos"])
print("Exibindo uma linha da planilha {0}".format(candidatoPorGenero))
print(dados.iloc[0])
print("Exibindo uma celula da planilha {0}".format(candidatoPorGenero))
print(dados.iloc[0]["Aptos"])
