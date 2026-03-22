"""
Me ajuda a resolver esse desafio de python

Sua tarefa é escrever uma função que encontre o menor caminho (o menor número de passos) entre dois pontos em uma rede de conexões. Isso é a base para algoritmos de GPS e roteamento de pacotes na internet.
​A Estrutura de Dados
​Você usará um Dicionário para representar um "Grafo Acíclico". As chaves são os nós (salas) e os valores são listas de nós conectados.
"""

from collections import deque

def menor_caminho(grafo, inicio, destino):
    if inicio == destino:
        return [inicio]
    
    fila = deque([(inicio, [inicio])])
    visitados = {inicio}
    
    while fila:
        no_atual, caminho = fila.popleft() 
        
        for vizinho in grafo.get(no_atual, []):
            if vizinho == destino:
                return caminho + [vizinho]
            
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))
    
    return None

def menor_numero_passos(grafo, inicio, destino):
    caminho = menor_caminho(grafo, inicio, destino)
    if caminho:
        return len(caminho) - 1
    return None

mapa_da_tumba = {
    'Entrada': ['Sala A', 'Sala B'],
    'Sala A': ['Entrada', 'Sala C', 'Sala D'],
    'Sala B': ['Entrada', 'Sala E'],
    'Sala C': ['Sala A'],
    'Sala D': ['Sala A', 'Tesouro'],
    'Sala E': ['Sala B', 'Tesouro'],
    'Tesouro': ['Sala D', 'Sala E']
}

resultado_caminho = menor_caminho(mapa_da_tumba, 'Entrada', 'Tesouro')
resultado_passos = menor_numero_passos(mapa_da_tumba, 'Entrada', 'Tesouro')

print(f"Caminho: {resultado_caminho}")
print(f"Passos: {resultado_passos}")
