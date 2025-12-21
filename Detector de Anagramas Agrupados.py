"""
Um anagrama é uma palavra formada pela transposição das letras de outra (ex: "amor", "roma" e "ramo").

Sua missão é criar uma função que receba uma lista de strings e agrupe as palavras que são anagramas entre si.

Exemplo de Entrada e Saída:
Entrada: ["amor", "roma", "carro", "arco", "ramo", "orca"]

Saída Esperada:

Python

[
  ["amor", "roma", "ramo"],
  ["carro"],
  ["arco", "orca"]
]
"""


def agrupar_anagramas(palavras):
    grupos = {}

    for palavra in palavras:
        chave = ''.join(sorted(palavra))
        if chave in grupos:
            grupos[chave].append(palavra)
        else:
            grupos[chave] = [palavra]
    return list(grupos.values())


# Teste com o exemplo
palavras = ["amor", "roma", "carro", "arco", "ramo", "orca"]
resultado = agrupar_anagramas(palavras)
print(resultado)