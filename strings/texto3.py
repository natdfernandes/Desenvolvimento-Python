with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    quantidade = texto.count("arquivo")

print(f"A palavra 'arquivo' aparece {quantidade} vezes no arquivo.")
