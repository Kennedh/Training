"""
O objetivo deste desafio é fazer uma função que some dois números inteiros sem utilizar os operadores + e -
"""

def sum_of_integers(a, b):
    # Máscara para limitar a 32 bits (evita loop infinito com negativos)
    mask = 0xFFFFFFFF
    
    # Aplica a máscara inicial
    a = a & mask
    b = b & mask
    
    while b != 0:
        carry = a & b
        a = (a ^ b) & mask        # Soma sem o carry, limitada a 32 bits
        b = (carry << 1) & mask   # Desloca o carry, limitado a 32 bits
        
    # Verifica se o resultado é um número negativo em 32 bits
    max_int = 0x7FFFFFFF
    
    # Se for positivo, retorna direto. Se for negativo, restaura o sinal pro padrão do Python.
    return a if a <= max_int else ~(a ^ mask)

# Testes
print(sum_of_integers(1000, 300))  # Saída: 1300
print(sum_of_integers(-1, 1))      # Saída: 0 
print(sum_of_integers(-5, -7))     # Saída: -12
