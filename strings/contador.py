with open("arquivo.txt", encoding="utf-8") as arquivo_texto:
    contador = 0
    print("Prévia arquivo")
    for linha in arquivo_texto:
        print(repr(linha))
        if linha:
            contador += 1
        print("total de linhas = ", contador)
