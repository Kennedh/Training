from datetime import datetime

def gerar_header_arquivo(dados):
    cod_banco = dados["banco"].zfill(3)
    lote = "0000"
    tipo_registro = "0"
    tipo_inscricao = dados["tipo_inscricao"]
    inscricao = dados["inscricao"].zfill(14)
    nome_empresa = dados["empresa"].ljust(30)
    convenio = dados["convenio"].ljust(20)
    nome_banco = dados["banco"].ljust(20)

    hoje = datetime.now()
    data_formatada = hoje.strftime("%d%m%Y")

    return (f"{cod_banco}{lote}{tipo_registro}{' ' * 9}{tipo_inscricao}{inscricao}{convenio}{nome_empresa}"
            f"{nome_banco}{' ' * 41}{data_formatada}").ljust(240)

def gerar_segmento_p(dados):

    banco = dados["banco"].zfill(3)
    lote = dados["lote"].zfill(4)
    tipo_registro = "3"
    num_doc = f"{dados['numero_documento']:0>15}"

    valor_int = int(dados["valor"] * 100)
    valor_formatado = f"{valor_int:0>15}"  # Supondo 15 posições no manual
    sequencial = dados["sequencial"].zfill(5)

    return f"{banco}{lote}{tipo_registro}{sequencial}'P'{' ' * 44}{num_doc}{valor_formatado}"


def gerar_arquivo_cnab(dados_empresa, lista_boletos):
    linhas = []
    header = gerar_header_arquivo(dados_empresa)
    linhas.append(header)

    for i, boleto in enumerate(lista_boletos, start=1):
        boleto["sequencial"] = str(i)
        linha_p = gerar_segmento_p(boleto)
        linhas.append(linha_p)

    return "\n".join(linhas)

