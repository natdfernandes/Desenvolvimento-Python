import csv

# abre arquivo csv

with open("teste1.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)  # Cria um leitor csv
    for linha in leitor:  # aletra sobre cada linha do arquivo
        print(linha)  # Cada linha é uma lista de strings

print("Nome do arquivo:", arquivo.name)
print("Modo do arquivo", arquivo.mode)
print("O arquivo está fechado?", arquivo.closed)
