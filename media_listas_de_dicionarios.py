"""
O objetivo é fazer uma função que calcule a média de uma lista de dicinários de estudantes. A chave é o estudante
e o valor é uma lista de notas.
"""

def calcula_media_dic(media):
    for dic in media:
        for chave, valor in dic.items():
            print(f"{chave} - Média: {sum(valor) / len(valor)}")


# Teste

dicc = [{"João":[9,8,7]},{"Maria":[6,7,2]}]

calcula_media_dic(dicc)

