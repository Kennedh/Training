"""
CONVERSOR DE IMAGENS NUMA PASTA PARA PDF

DEIXEI EXPLICADO A CADA PONTO PARA FICAR CLARO NA REVISÃO

"""

import os
from PIL import Image


def converter_imagens_para_pdf(diretorio_origem, diretorio_destino):
    # Verifica se a pasta de destino existe, se não, cria
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    # Extensões de imagem aceitas
    extensoes_validas = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio_origem)

    print(f"Iniciando conversão de imagens em: {diretorio_origem}...\n")

    count = 0
    for arquivo in arquivos:
        # Verifica se o arquivo termina com uma extensão de imagem válida
        if arquivo.lower().endswith(extensoes_validas):
            caminho_completo = os.path.join(diretorio_origem, arquivo)

            try:
                # 1. Abre a imagem
                imagem = Image.open(caminho_completo)

                # 2. Converte para RGB
                # (Essencial para converter PNGs transparentes para PDF, senão dá erro)
                imagem = imagem.convert('RGB')

                # 3. Define o nome do novo arquivo PDF
                nome_sem_extensao = os.path.splitext(arquivo)[0]
                nome_pdf = f"{nome_sem_extensao}.pdf"
                caminho_pdf = os.path.join(diretorio_destino, nome_pdf)

                # 4. Salva como PDF
                imagem.save(caminho_pdf)
                print(f"Convertido: {arquivo} -> {nome_pdf}")
                count += 1

            except Exception as e:
                print(f"Erro ao converter {arquivo}: {e}")

    print(f"\nSucesso! Total de {count} imagens convertidas.")


# --- Configuração ---
# Substitua pelo caminho da sua pasta de imagens
pasta_entrada = "C:\pdf"
pasta_saida = "C:\pdf-feito"

# Executa a função
converter_imagens_para_pdf(pasta_entrada, pasta_saida)