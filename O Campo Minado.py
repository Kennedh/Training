"""
Imagine que você tem um tabuleiro de Campo Minado. Você recebe uma matriz onde o número 9 representa uma bomba e o
número 0 representa um espaço vazio.

Sua missão é criar uma função que transforme esse tabuleiro, substituindo os 0 pela quantidade de bombas adjacentes
(ao redor) daquela célula.

Regras:
Uma célula deve checar todas as 8 posições vizinhas (horizontal, vertical e diagonais).

Se a célula for uma bomba (9), ela permanece como 9.

Se for 0, ela vira a soma de bombas ao redor.

Exemplo de Entrada e Saída:
Entrada (Matriz 3x3):

Python

tabuleiro = [
    [9, 0, 0],
    [0, 0, 0],
    [9, 0, 9]
]
Saída Esperada:

Python

[
    [9, 1, 0],
    [2, 3, 2],
    [9, 2, 9]
]
(Repare que o centro virou 3 porque tem bombas no topo-esquerdo, baixo-esquerdo e baixo-direito).
"""


def calcular_dicas(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    resultado = [linha[:] for linha in matriz]

    direcoes = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == 9:
                continue

            bombas_ao_redor = 0

            for dx, dy in direcoes:
                novo_i, novo_j = i + dx, j + dy

                if 0 <= novo_i < linhas and 0 <= novo_j < colunas:
                    if matriz[novo_i][novo_j] == 9:
                        bombas_ao_redor += 1

            resultado[i][j] = bombas_ao_redor

    return resultado


# Teste
campo = [
    [9, 0, 0],
    [0, 0, 0],
    [9, 0, 9]
]
print(calcular_dicas(campo))