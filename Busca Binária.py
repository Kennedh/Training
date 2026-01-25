"""
Você recebe uma lista de números já ordenados (crescente) e um número target. Você deve retornar o índice (posição)
onde o target está. Se ele não existir na lista, retorne -1.

A Regra: Você não pode usar nums.index() nem um loop for simples que olha um por um. Você deve usar a lógica de dividir
para conquistar.

Olhe o meio da lista.

É o número que eu quero? Achou!

O número do meio é maior que o alvo? Então jogue a metade da direita fora (o alvo só pode estar na esquerda).

O número do meio é menor que o alvo? Jogue a metade da esquerda fora.

Repita.
"""


def busca_binaria(nums, target):
    esquerda = 0
    direita = len(nums) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        chute = nums[meio]
        if chute == target:
            return meio
        elif chute > target:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1


# --- TESTES ---
testes = [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([5], 5, 0),
    ([2, 5], 5, 1)
]

print(f"{'LISTA':<20} | {'ALVO':<5} | {'RES':<5} | {'STATUS'}")
print("-" * 50)
for lista, alvo, esperado in testes:
    res = busca_binaria(lista, alvo)
    status = "✅" if res == esperado else "❌"
    print(f"{str(lista):<20} | {alvo:<5} | {res:<5} | {status} (Esp: {esperado})")