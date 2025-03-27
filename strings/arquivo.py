with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip("#, ")
        print(linha_limpa)
