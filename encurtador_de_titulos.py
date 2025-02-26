"""
Crie uma função chamada shorten_dickens_titles que receba títulos e max_length como parâmetros.

Esta função tem como objetivo encurtar os títulos dos romances de Dickens para um comprimento máximo especificado,
para ajudar os participantes do Dickens Festival a identificar rapidamente os livros.

O parâmetro titles é uma matriz de strings, onde cada string representa o título de um romance de Dickens.
O parâmetro max_length é um inteiro que especifica o comprimento máximo permitido para cada título encurtado.

Para encurtar um título, remova caracteres do final do título até que o comprimento seja igual ou menor que max_length.
Se o título encurtado for estritamente menor que max_length, anexe reticências (...) ao final para indicar o truncamento
Se o título original já for menor ou igual a max_length, nenhuma alteração deve ser feita.
"""

def shorten_dickens_titles(titles, max_length):
    result = []
    for title in titles:
        if len(title) < max_length:
            result.append(f'{title[:max_length]}...')
        else:
            result.append(f'{title[:max_length]}')
    return result

# Teste

print(shorten_dickens_titles(["Oliver Twist", "A Tale of Two Cities"],5))

