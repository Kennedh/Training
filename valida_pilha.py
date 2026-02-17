"""
Você deve criar uma função que verifica se os parenteses, colchetes e chaves de uma expressão 
matemática estão balanceados corretamente.
"""

def verifica_pilha_simbols(strng):
    abre = ["(", "[", "{"]
    fecha = {")":"(", "]":"[", "}":"{"}
    pilha = []

    for simbol in strng:
        if simbol in abre:
            pilha.append(simbol)
        elif simbol in fecha:
            if not pilha:
                return False
            if pilha[-1] == fecha[simbol]:
                pilha.pop()
            else:
                return False
    return len(pilha) == 0
                     

# Teste

print(verifica_pilha_simbols("({)}"))
print(verifica_pilha_simbols("({})"))
print(verifica_pilha_simbols("{[()]}"))
print(verifica_pilha_simbols("{[()]"))