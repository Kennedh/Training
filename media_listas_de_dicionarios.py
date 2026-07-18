"""
O objetivo é fazer uma função que calcule a média de uma lista de dicinários de estudantes. A chave é o estudante
e o valor é uma lista de notas.
"""

def calcula_media_dic(estudantes):
    """
    Calcula e exibe a média das notas de cada estudante.
    
    Args:
        estudantes: Lista de dicionários no formato [{"nome": [notas]}, ...]
    """
    for estudante in estudantes:
        for nome, notas in estudante.items():
            if not notas:  # Evita divisão por zero
                media = 0
            else:
                media = sum(notas) / len(notas)
            print(f"{nome} - Média: {media:.2f}")  # Formata com 2 casas decimais


# Teste
dicc = [{"João": [9, 8, 7]}, {"Maria": [6, 7, 2]}]
calcula_media_dic(dicc)