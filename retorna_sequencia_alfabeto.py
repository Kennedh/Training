"""
Fazer uma função que receba um número de 1 a 26 e retorne o alfabeto até a respectiva letra/posição.
"""

def retorna_seq_alfatbeto(pos):
    alf_str = "abcdefghijklmnopqrstuvxwyz"
    alfabeto = list(alf_str)
    for letra in alfabeto:
        if alfabeto.index(letra) <= pos-1:
            print(letra)

# Teste

retorna_seq_alfatbeto(37)