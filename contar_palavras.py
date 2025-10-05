"""
O Desafio: Escreva uma função chamada contar_palavras que receba o caminho de um arquivo de texto (caminho_arquivo)
como argumento.

Regras:

A função deve ler o conteúdo do arquivo.

Ela deve contar a frequência de cada palavra no texto.

A contagem não deve diferenciar letras maiúsculas de minúsculas (ou seja, "Python" e "python" devem ser contados como
a mesma palavra).

A função deve ignorar pontuações básicas como vírgula (,), ponto final (.), exclamação (!) e interrogação (?).

A função deve retornar um dicionário onde as chaves são as palavras e os valores são suas contagens, ordenado da
palavra mais frequente para a menos frequente.

Exemplo: Se um arquivo de texto contiver a frase "Olá mundo! Este é um teste. Olá novamente, mundo.", o retorno
esperado seria algo como:

Python

{'olá': 2, 'mundo': 2, 'este': 1, 'é': 1, 'um': 1, 'teste': 1, 'novamente': 1}
"""

def contar_palavras(caminho):
    res = {}
    with open(caminho) as t:
        p = t.read()
        palavras = p.lower().split(" ")

    for palavra in palavras:
        res[palavra] = res.get(palavra, 0) + 1

    lista_ordenada = sorted(res.items(),key=lambda item: item[1], reverse=True)
    return dict(lista_ordenada)

print(contar_palavras("texto_desafio.txt"))

