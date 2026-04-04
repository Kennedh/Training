"""
Dada uma lista de dígitos, retorne o maior número que pode ser formado a partir desses dígitos, usando cada dígito apenas uma vez (ignorando duplicatas). Apenas números positivos no intervalo de 1 a 9 serão passados para a função.
"""

def max_value(digits):
    return int("".join(map(str, sorted(set(digits), reverse=True))))


# Testes

print(max_value([1, 3, 1]))           # Saída: 31
print(max_value([5, 7, 5, 9, 7]))     # Saída: 975
print(max_value([1, 9, 3, 1, 7, 4, 6, 6, 7]))  # Saída: 976431