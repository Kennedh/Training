"""
Entrada: Duas strings representando números inteiros não negativos (ex: '123', '45'). Saída: Uma string representando o
produto (ex: '5535').
Regra: Você não pode converter as strings inteiras para int() de uma vez. Precisa manipular os dígitos.
"""

def multiplica_strings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            pos1 = i + j
            pos2 = i + j + 1
            total = mul + result[pos2]
            result[pos2] = total % 10
            result[pos1] += total // 10
    result_str = ''.join(str(digit) for digit in result)
    result_str = result_str.lstrip('0')
    return result_str if result_str else "0"

# Teste

print(multiplica_strings("123", "45"))
print(multiplica_strings("2", "3"))
print(multiplica_strings("123", "456"))
print(multiplica_strings("0", "123"))
print(multiplica_strings("999", "999"))

