"""
O Desafio: Escreva um decorator em Python chamado cache_resultado.

Regras:

O decorator deve armazenar ("cachear") o resultado de uma função baseando-se nos argumentos com os quais ela foi
chamada.

Na primeira vez que a função for chamada com um conjunto específico de argumentos, ela deve executar normalmente e o
decorator deve salvar o resultado.

Se a mesma função for chamada novamente com exatamente os mesmos argumentos, o decorator deve retornar o resultado
salvo anteriormente, sem executar a função novamente.

O decorator deve funcionar para funções com qualquer número de argumentos posicionais e nomeados.

Para simplificar, você pode assumir que os argumentos da função serão "hasheáveis" (ou seja, podem ser usados como
chaves de dicionário).

Exemplo de uso:

Python

@cache_resultado
def fibonacci(n):
    print(f"Calculando fibonacci({n})...")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Primeira chamada - deve calcular e imprimir a mensagem
print(fibonacci(5))

# Segunda chamada com o mesmo argumento - não deve imprimir a mensagem,
# deve retornar o resultado do cache instantaneamente.
print(fibonacci(5))
"""

import time

def cache_resultado(func):
    cache = {}
    def wrapper(*args, **kwargs):
        print(f"Buscando valor: {args[0]}")
        chave = args
        if chave in cache:
            print("Encontrou valor")
            return cache[chave]
        resultado = func(*args, **kwargs)
        cache[chave] = resultado
        print("Não encontrou o valor")
        return resultado
    return wrapper


@cache_resultado
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1))
print(fibonacci(1))
print(fibonacci(2))

