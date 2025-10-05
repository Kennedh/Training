"""
O Desafio: Escreva uma função em Python chamada fizz_buzz.

Regras:

A função deve receber um número inteiro (n) como argumento.

Ela deve iterar de 1 até n (inclusive).

Para cada número na iteração:

Se o número for divisível por 3 e 5 ao mesmo tempo, imprima "FizzBuzz".

Se o número for divisível apenas por 3, imprima "Fizz".

Se o número for divisível apenas por 5, imprima "Buzz".

Caso contrário, imprima o próprio número.

Exemplo de execução: fizz_buzz(15) deve imprimir:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""

def fizz_buzz(n):
    res = ["1"]
    for i in range(1,n + 1):
        if i % 3 == 0 or i % 5 == 0:
            res.append("Fizz")
        else:
            res.append(str(i))
    return "\n".join(res) + "Buzz" if res[-1] == "Fizz" else "\n".join(res)

# Teste

print(fizz_buzz(15))
