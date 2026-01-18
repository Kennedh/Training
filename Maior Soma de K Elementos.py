"""
O Conceito: Janela Deslizante (Sliding Window)
Imagine que você tem uma régua com um buraco retangular no meio. Você coloca essa régua sobre uma fita de números.
Você só consegue ver k números por vez. Para ver os próximos, você não tira a régua e coloca de novo; você a desliza
uma posição para a direita.

Dada uma lista de números e um tamanho k, encontre a maior soma possível de k números consecutivos.

Exemplo: nums = [1, 4, 2, 10, 23, 3, 1, 0, 20] k = 4

Primeira janela [1, 4, 2, 10]. Soma = 17.

Desliza! Sai o 1, entra o 23.

Nova janela [4, 2, 10, 23]. Soma = 17 - 1 + 23 = 39.

E assim por diante...

Sua Missão: Complete o código abaixo. O segredo é fazer isso com um único loop (depois de calcular a primeira janela).
"""


def max_soma_sublista(nums, k):
    if len(nums) < k:
        return None
    soma_atual = sum(nums[:k])
    max_soma = soma_atual
    for i in range(k, len(nums)):
        soma_atual = soma_atual + nums[i] - nums[i - k]
        if max_soma < soma_atual:
            max_soma = soma_atual
    return max_soma


# --- TESTES ---
testes = [
    ([1, 4, 2, 10, 23, 3, 1, 0, 20], 4, 39),
    ([100, 200, 300, 400], 2, 700),
    ([1, 4, 2, 10, 2, 3, 1, 0, 20], 4, 24),
]

for lista, k, esperado in testes:
    resultado = max_soma_sublista(lista, k)
    print(f"Lista: {str(lista)} | k={k} | Resultado: {resultado} | Esperado: {esperado}")