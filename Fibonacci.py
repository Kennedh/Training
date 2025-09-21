"""Que tal um desafio de matemática e programação que é super popular? A sequência de Fibonacci 🐇.

É uma sequência numérica onde cada número é a soma dos dois anteriores. Ela começa com 0 e 1, e continua assim:
0,1,1,2,3,5,8,....

O nosso objetivo é criar um programa em Python que possa gerar os primeiros números dessa sequência.

E depois fazer outra função para calcular a fibonacci de forma recursiva para trazer o n ésimo número da sequencia """

def fibonacci(n):
    res = [0,1]
    if n == 1:
        return [0]
    elif n == 0:
        return []
    elif n == 2:
        return res
    else:
        for i in range(n-2):
            res.append(res[-1] + res[-2])
        return res

def fibonacci_recursivo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Teste


print(fibonacci(8))
print(fibonacci_recursivo(7))
