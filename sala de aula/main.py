from PIL import Image
import os


# função para carregar imagem e converte-la para binário 1 usage
def carregar_imagem_para_binario(caminho_imagem):
    # Abre a imagem
    imagem = Image.open(caminho_imagem)

    # Converte a imagem para modo 'L' (escala de cinza) para simplificar
    imagem = imagem.convert("L")

    # Exibe a imagem original
    imagem.show(title="Imagem Original")

    # Converte a imagem para bytes
    dados_binarios = imagem.tobytes()

    return dados_binarios, imagem.size


# Função para salvar dados binários em um arquivo 2 usages
def salvar_binario_em_arquivo(dados_binarios, caminho_arquivo):
    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_binarios)
    print(f"Dados binários salvos em' {caminho_arquivo}'")


# Função para copiar um arquivo binário
def copiar_arquivo_binario(caminho_origem, caminho_destino):
    with open(caminho_origem, "rb") as origem, open(caminho_destino, "wb") as destino:
        destino.write(origem.read())
    print(f"Arquivo copiado para '{caminho_destino}'.")


# Função para manipular os dados binários (inverter os bytes)
def manipular_dados_binarios(caminho_arquivo):
    with open(caminho_arquivo, "rb") as arquivo:
        dados = bytearray(arquivo.read())  # Lê os dados como bytearray para manipulação
    # Inverte os bythes (exemplo de manipulação)
    dados_invertidos = bytearray([255 - byte for byte in dados])
    return dados_invertidos


def carregar_imagem_de_binario(dados_binarios, tamanho_imagem):
    """
    Reconstrói uma imagem a partir de dados binários e salva como arquivo.

    Args:
        dados_binarios: Bytes contendo os dados da imagem
        tamanho_imagem: Tupla (largura, altura) com as dimensões originais
    """
    # Criar uma nova imagem em modo escala de cinza (L)
    imagem = Image.new("L", tamanho_imagem)

    # Carregar os dados binários na imagem
    imagem.frombytes(dados_binarios)

    # Exibir a imagem reconstruída
    imagem.show(title="Imagem Reconstruída")

    return imagem


# Função principal
def main():
    # Caminho de imagem original
    caminho_imagem = "imagem.jpg"  # substitua pelo caminho da sua imagem
    if not os.path.exists(caminho_imagem):
        print(f"Arquivo '{caminho_imagem}' não encontrado.")
        return

    # 1. Carregar a imagem e converter para binário
    dados_binarios, tamanho_imagem = carregar_imagem_para_binario(caminho_imagem)

    # 2. Exibir os dados binários (apenas os primiros 100 bytes para exemplo)
    print("Dados binários (primeiros 100 bytes):", dados_binarios[:100])

    # 3. Salvar os dados binários em um arquivo
    caminho_binario_original = "imagem_binaria.dat"
    salvar_binario_em_arquivo(dados_binarios, caminho_binario_original)

    # 4. Fazer uma cópia do arquivo binário
    caminho_binario_copia = "imagem_binaria_copia.dat"
    copiar_arquivo_binario(caminho_binario_original, caminho_binario_copia)

    # 5. Manipular os dados do arquivo binário cópia (inverter os bytes)
    dados_manipulados = manipular_dados_binarios(caminho_binario_copia)

    # 6. Salvar os dados manipulados em um novo arquivo
    caminho_binario_manipulado = "imagem_manipulado.dat"
    salvar_binario_em_arquivo(dados_manipulados, caminho_binario_manipulado)

    # 7. Carregar a imagem modificada a partir dos dados binários manipulados
    imagem_reconstruida = carregar_imagem_de_binario(dados_manipulados, tamanho_imagem)
    imagem_reconstruida.save("imagem_reconstruida.png")


# Executa o programa
if __name__ == "__main__":
    main()
