"""
Faça uma função que criptografe um texto em que transforme as letras nas suas respectivas posições no alfabeto
"""

alfabeto_extenso = "abcdefghijklmnopqrstuvxwyz"
alfabeto = list(alfabeto_extenso)
criptografado = []

def criptograf_texto(texto):
    global alfabeto
    global criptografado
    alfabeto = list(alfabeto_extenso)
    lista = list(texto)
    for letra in lista:
        if letra == " ":
            criptografado.append(0)
        else:
            criptografado.append(alfabeto.index(letra)+1)


def descriptograf_texto(texto):
    retorno = ""
    global alfabeto
    global criptografado
    for xar in criptografado:
        retorno += str(alfabeto[xar-1])
    print(retorno)

aalfabeto_extenso = "abcdefghijklmnopqrstuvxwyz"
aalfabeto = list(aalfabeto_extenso)

criptograf_texto("kennedh")

print(criptografado)

descriptograf_texto(criptografado)


# print(aalfabeto.index("n")+1)

# 1151414548


