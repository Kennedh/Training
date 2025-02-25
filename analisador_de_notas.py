"""
📌 Desafio: Analisador de Notas
Você deve criar um programa que receba várias notas de alunos e retorne um dicionário com informações sobre essas notas.

Requisitos:
Crie uma função chamada analisar_notas que recebe um número variável de notas (usando *args).
O programa deve retornar um dicionário contendo:
Quantidade de notas recebidas.
Média das notas.
Maior nota.
Menor nota.
Situação:
Se a média for ≥ 7 → "Aprovado"
Se a média for ≥ 5 e < 7 → "Recuperação"
Se a média for < 5 → "Reprovado"
"""

def analisar_notas(*args):
    analise = {}
    analise_texto = ""
    qtde_notas = len(args)
    analise["Quantidade"] = qtde_notas
    media = sum(args) / qtde_notas
    analise["Média"] = media
    maior_nota = max(args)
    analise["Maior_nota"] = maior_nota
    menor_nota = min(args)
    analise["Menor_nota"] = menor_nota
    if media >= 7:
        analise["Situação"] = "Aprovado"
    else:
        analise["Situação"] = "Reprovado"
    for chave, valor in analise.items():
        analise_texto += f"{chave}: {valor}\n"
    return analise_texto

print(analisar_notas(7,8,9,5,6))

