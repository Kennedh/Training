"""
Crie um programa que leia um arquivo e conte:

- O número total de caracteres;
- O número total de palavras;
- O número de ocorrências de cada palavra.
"""
from collections import Counter

with open("palavras.txt") as f:
    texto = f.read()
    w = len(texto.splitlines())
    texto_limpo = texto.replace("\n", "")
    l = list(texto_limpo)
    total_letras = len(l)
    palavras = texto.splitlines()

    contador = Counter(palavras) # Conta a quantidade de ocorrências de cada palavra

print(f"Total de palavras: {w}")
print(f"Total de letras: {total_letras}")

print(contador)
