try:
    # Tentativa de abrir e manipular o arquivo
    arquivo = open("dado.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
except PermissionError:
    print("Erro: Permissão negada para acessar o arquivo!")
except IndexError as e:
    print(f"Erro de E/S: {e}")
finally:
    # Garante que o arquivo será fechado
    if "arquivo" in locals():
        arquivo.close
