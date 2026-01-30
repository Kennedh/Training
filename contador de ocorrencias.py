"""
Criar uma função que conte quantas vezes cada número aparece em uma lista.

Entrada esperada:
numeros = [1, 2, 2, 3, 3, 3, 4]

Saída esperada:
{
    1: 1,
    2: 2,
    3: 3,
    4: 1
}

⚠️ Regras

✔️ Use apenas list e dict

❌ Não use Counter do collections

❌ Não use set
"""

def contar_ocorrencias(lista):
    res = {}
    for num in lista:
        if num in res:
            res[num] += 1
        else:
            res[num] = 1
    return res

# Teste

print(contar_ocorrencias([1, 2, 2, 3, 3, 3, 4]))
