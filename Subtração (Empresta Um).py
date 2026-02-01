"""
Agora que você domina o "vai-um" (carry) da soma e da multiplicação, vamos para o inverso.

O Desafio: Dado duas strings representando números inteiros positivos, retorne a string da subtração (num1 - num2).

Pode assumir que num1 será sempre maior ou igual a num2 (para não precisarmos lidar com números negativos ou sinais agora).

Você não pode converter para int direto.

A Dica de Ouro: Na soma, se a + b > 9, a gente faz o carry (+1 na esquerda) e guarda o resto (% 10). Na subtração,
se a - b < 0, a gente precisa emprestar (-1 da esquerda) e somar 10 ao número atual.

Quer tentar implementar essa lógica do "emprestar"?
"""


def subtract_strings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    result = []
    borrow = 0
    while i >= 0 or j >= 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        digit1 -= borrow
        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
        current_digit = digit1 - digit2
        result.append(str(current_digit))
        i -= 1
        j -= 1
    result_str = ''.join(result[::-1]).lstrip('0')
    return result_str if result_str else "0"


# Testando a função
if __name__ == "__main__":
    # Testes
    print(subtract_strings("100", "1"))  # "99"
    print(subtract_strings("50", "25"))  # "25"
    print(subtract_strings("1000", "1"))  # "999"
    print(subtract_strings("123", "123"))  # "0"
    print(subtract_strings("9876", "5432"))  # "4444"
    print(subtract_strings("100", "99"))  # "1"

    # Caso mais complexo com múltiplos emprestimos
    print(subtract_strings("1000", "999"))  # "1"
    print(subtract_strings("2000", "1999"))  # "1"