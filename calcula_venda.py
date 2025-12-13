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
    faturamento = 0
    produtos_unicos = []
    mais_vendido = {}
    res = {}

    for venda in vendas:
        total_itens += venda.get("quantidade")
        faturamento += venda.get("quantidade") * venda.get("valor_unitario")
        produtos_unicos.append(venda.get("produto"))
        mais_vendido[venda.get("produto")] = venda.get("quantidade")

    res["total_itens"] = total_itens
    res["faturamento"] = faturamento
    res["produtos_unicos"] = set(produtos_unicos)
    res["mais_vendido"] = sorted(mais_vendido, reverse=True)[0]

    return res

# Teste

print(calcula_venda(vendas = [
    {"produto": "maçã", "quantidade": 10, "valor_unitario": 2.5},
    {"produto": "banana", "quantidade": 5, "valor_unitario": 3.0},
    {"produto": "maçã", "quantidade": 4, "valor_unitario": 2.5}
]))


