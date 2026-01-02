"""
Imagine que você recebeu um texto cheio de abreviações de um chat e precisa limpar isso para um relatório formal.
Você tem uma tabela (dicionário) que diz o que cada gíria significa.

📝 O Problema
Crie uma função que receba duas coisas:

Uma string (a frase com gírias).

Um dicionário (onde a chave é a gíria e o valor é a palavra correta).

A função deve retornar a frase traduzida. Se uma palavra da frase não estiver no dicionário, mantenha ela como está.
"""

def traduz_giria(texto):
    girias = {
        "vc": "você",
        "tb": "também",
        "eh": "é",
        "pq": "porque"
    }
    return " ".join([girias[palavra] if palavra in girias else palavra for palavra in texto.split()])

# Teste

print(traduz_giria("vc eh legal"))
print(traduz_giria("eu vou tb"))
print(traduz_giria("pq vc não foi"))
