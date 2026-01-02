"""
Imagine que você tem duas planilhas de clientes. Uma lista veio do Marketing e a outra veio do Financeiro. Você precisa
descobrir quais clientes estão nas duas listas ao mesmo tempo.📝 O ProblemaCrie uma função que receba duas listas de
números (ou nomes) e retorne uma nova lista contendo apenas os elementos que aparecem em ambas.O resultado não precisa
estar ordenado e não deve conter duplicatas (mesmo que a lista original tenha).
Lista 1,Lista 2,Saída Esperada
"[1, 2, 3, 4]","[3, 4, 5, 6]","[3, 4]"
"[10, 20]","[30, 40]",[] (Vazia)
"[""Naruto"", ""Sasuke""]","[""Sakura"", ""Naruto""]","[""Naruto""]"
"[1, 1, 2]","[1, 3]",[1] (Sem repetidos)
"""

def list_intersect(l1, l2):
    l1, l2 = set(l1), set(l2)
    return list(l1 & l2)

# Teste

print(list_intersect([1, 2, 3, 4],[3, 4, 5, 6]))


