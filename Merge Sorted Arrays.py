"""
Você tem duas listas de números lista1 e lista2, que já estão ordenadas do menor para o maior. Sua missão é fundir
(merge) as duas em uma única lista, que também deve ficar ordenada.

A Regra de Ouro: 🚫 Você NÃO pode usar sorted() ou .sort(). O objetivo é criar a lógica de intercalação manualmente.
(Imagine que são duas pilhas de cartas na mesa e você quer criar uma pilha única pegando sempre a menor carta disponível
no topo de cada uma).
"""

def mesclar_listas(l1, l2):
    x = 0
    y = 0
    res = []
    if len(l1) < 1:
        return l2
    elif len(l2) < 1:
        return l1
    while x < len(l1) and y < len(l2):
        if l1[x] < l2[y]:
            res.append(l1[x])
            x += 1
        else:
            res.append(l2[y])
            y += 1
        if x == len(l1) and y != len(l2):
            res.extend(l2[y:])
        elif y == len(l2) and x != len(l1):
            res.extend(l1[x:])
    return res

# Teste

testes = [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [0], [0]),
    ([5, 10], [1, 2, 3], [1, 2, 3, 5, 10]), # Uma lista maior que a outra
    ([1, 1], [1, 1], [1, 1, 1, 1])
]

for l1, l2, esperado in testes:
    res = mesclar_listas(l1, l2)
    print(f"L1: {l1} + L2: {l2} -> {res} | {'✅' if res == esperado else '❌'}")