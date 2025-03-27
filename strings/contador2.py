with open("arquivo.txt", encoding="utf-8") as arquivo_texto:
    contador = 0
    print("Novo arquivo")
    for linha in arquivo_texto:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
        if linha_limpa:
            contador += 1
    print("Total de linhas =", contador)
