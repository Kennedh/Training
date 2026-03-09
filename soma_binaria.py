"""
O objetivo deste desafio é fazer uma função que some dois números inteiros sem utilizar os operadores + e -
"""

def sum_of_integers(a, b):
    while b != 0:
        carry = a & b
        a     = a ^ b
        b     = carry << 1
    return a

# Teste

print(sum_of_integers(1000,300))