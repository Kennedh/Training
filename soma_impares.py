"""
Crie uma função que receba uma lista de números inteiros e retorne a soma dos números ímpares.
"""

def soma_impar(numeros):
    return sum([num for num in numeros if num % 2 != 0])

# Teste

print(soma_impar([2,3,4,5,6,7,8,9,10]))