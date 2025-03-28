"""
Faça uma função que criptografe um texto em que transforme as letras nas suas respectivas posições no alfabeto
"""

def criptograf_texto(texto):
    alfabeto_extenso = "abcdefghijklmnopqrstuvxwyz"
    alfabeto = list(alfabeto_extenso)
    criptografado = ""
    lista = list(texto)
    for letra in lista:
        if letra == " ":
            criptografado += "0"
        else:
            criptografado += str(alfabeto.index(letra)+1)
    return criptografado


aalfabeto_extenso = "abcdefghijklmnopqrstuvxwyz"
aalfabeto = list(aalfabeto_extenso)

print(criptograf_texto("kennedh"))

print(aalfabeto.index("n")+1)

# 1151414548


