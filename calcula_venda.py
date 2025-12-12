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

    for venda in vendas:
        temp = [a for a in venda]

# Teste
