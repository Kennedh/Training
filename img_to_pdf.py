"""
CONVERSOR DE IMAGENS NUMA PASTA PARA PDF

DEIXEI EXPLICADO A CADA PONTO PARA FICAR CLARO NA REVISÃO

"""
import os
from PIL import Image


def converter_imagens(diretorio_origem, diretorio_destino, um_arquivo_so=True):
    """
    Converte imagens para PDF.
    :param um_arquivo_so: Se True, gera um único PDF com todas as imagens.
                          Se False, gera um PDF para cada imagem.
    """
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    extensoes_validas = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    # Filtra e ordena os arquivos (importante para o PDF único não vir bagunçado)
    arquivos = [f for f in os.listdir(diretorio_origem) if f.lower().endswith(extensoes_validas)]
    arquivos.sort()

    if not arquivos:
        print("Nenhuma imagem encontrada.")
        return

    print(f"Iniciando processamento de {len(arquivos)} imagens...")

    imagens_processadas = []

    for arquivo in arquivos:
        caminho_img = os.path.join(diretorio_origem, arquivo)
        try:
            img = Image.open(caminho_img).convert('RGB')

            if um_arquivo_so:
                imagens_processadas.append(img)
            else:
                # Salva individualmente na hora
                nome_pdf = os.path.splitext(arquivo)[0] + ".pdf"
                img.save(os.path.join(diretorio_destino, nome_pdf))
                print(f"Individual: {arquivo} -> {nome_pdf}")

        except Exception as e:
            print(f"Erro em {arquivo}: {e}")

    # Se a opção for arquivo único, salva a lista acumulada aqui
    if um_arquivo_so and imagens_processadas:
        nome_final = os.path.join(diretorio_destino, "unificado.pdf")
        # O truque da Pillow: salva a primeira e anexa o resto
        primeira = imagens_processadas.pop(0)
        primeira.save(nome_final, save_all=True, append_images=imagens_processadas, optimize=True, quality=40)
        print(f"\nSucesso! PDF único gerado em: {nome_final}")

    elif not um_arquivo_so:
        print(f"\nSucesso! {len(arquivos)} PDFs individuais gerados.")


# --- Configuração ---
pasta_entrada = r"C:\pdf"
pasta_saida = r"C:\pdf-feito"

# Escolha: True para um PDF só, False para vários
converter_imagens(pasta_entrada, pasta_saida, um_arquivo_so=True)