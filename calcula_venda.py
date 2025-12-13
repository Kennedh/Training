"""
Crie uma função chamada analisa_vendas que recebe uma lista de vendas, onde cada venda é um dicionário no formato:

{
    "produto": str,
    "quantidade": int,
    "valor_unitario": float
}


A função deve retornar outro dicionário com as seguintes informações:

total_itens → soma total das quantidades

faturamento → soma de (quantidade * valor_unitario)

produtos_unicos → conjunto (set) com os nomes dos produtos

mais_vendido → nome do produto com maior quantidade somada

Exemplo de entrada
vendas = [
    {"produto": "maçã", "quantidade": 10, "valor_unitario": 2.5},
    {"produto": "banana", "quantidade": 5, "valor_unitario": 3.0},
    {"produto": "maçã", "quantidade": 4, "valor_unitario": 2.5}
]

O que você deve devolver
{
    "total_itens": ...,
    "faturamento": ...,
    "produtos_unicos": ...,
    "mais_vendido": ...
}
"""

def calcula_venda(vendas):
    total_itens = 0
    faturamento = 0.0
    produtos_unicos = set()
    contagem_por_produto = {}

    for venda in vendas:
        produto = venda.get("produto")
        qtd = venda.get("quantidade")
        valor = venda.get("valor_unitario")
        total_itens += qtd
        faturamento += qtd * valor
        produtos_unicos.add(produto)

        if produto in contagem_por_produto:
            contagem_por_produto[produto] += qtd
        else:
            contagem_por_produto[produto] = qtd

    produto_campeao = max(contagem_por_produto, key=contagem_por_produto.get)

    return {
        "total_itens": total_itens,
        "faturamento": faturamento,
        "produtos_unicos": produtos_unicos,
        "mais_vendido": produto_campeao
    }

# Teste

print(calcula_venda(vendas = [
    {"produto": "maçã", "quantidade": 10, "valor_unitario": 2.5},
    {"produto": "banana", "quantidade": 5, "valor_unitario": 3.0},
    {"produto": "maçã", "quantidade": 4, "valor_unitario": 2.5}
]))


