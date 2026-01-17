"""
Dada uma lista de números inteiros, mova todos os 0 para o final da lista, mantendo a ordem original dos números
que não são zero.

Regras:

Você deve fazer isso na própria lista nums (não pode fazer return de uma nova lista).

Tente minimizar o número de operações.

Exemplo:

Python

entrada = [0, 1, 0, 3, 12]
# Processamento...
# Saída esperada: [1, 3, 12, 0, 0]
"""


def move_zeros(nums):
    posicao_troca = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[posicao_troca], nums[i] = nums[i], nums[posicao_troca]
            posicao_troca += 1


# --- TESTES ---
lista1 = [0, 1, 0, 3, 12]
move_zeros(lista1)
print(f"Resultado: {lista1} | Esperado: [1, 3, 12, 0, 0]")

lista2 = [0]
move_zeros(lista2)
print(f"Resultado: {lista2} | Esperado: [0]")

lista3 = [4, 2, 9]  # Sem zeros
move_zeros(lista3)
print(f"Resultado: {lista3} | Esperado: [4, 2, 9]")