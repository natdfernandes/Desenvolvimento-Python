import csv

dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', '25', 'São Paulo'],
    ['Maria', '40', 'Rio de Janeiro'],
    ['Ana', '25', 'Campinas']
]

# Abre o arquivo csv para escrita

with open('arquivo_saida.csv', mode='w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo) #cria um escritor de csv
    escritor.writerows(dados) #escreve todas as linhas de uma vez