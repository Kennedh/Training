"""
Um palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente (como "Arara" ou "Ovo").
​📝 O Problema
​Crie uma função que receba uma string e retorne True se ela for um palíndromo e False caso contrário.
​O "Pulo do Gato" (A pegadinha):
Sua função deve ignorar espaços em branco e diferenças entre maiúsculas/minúsculas.
Ou seja, para o computador, "Ame o poema" deve ser considerado um palíndromo válido, mesmo tendo espaços e o "A" maiúsculo no começo.
"""

def eh_palindromo(texto):
    texto_tratado = texto.replace(" ", "").lower()
    return texto_tratado == texto_tratado[::-1]

# Teste

print(eh_palindromo("python"))
print(eh_palindromo("arara"))