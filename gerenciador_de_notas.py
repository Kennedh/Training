"""
📌 Objetivo: Criar um sistema de notas onde o usuário pode adicionar, remover e calcular a média das notas.

🔹 Conceitos usados:
✔ Listas e operações básicas
✔ Funções (adicionar_nota(), remover_nota(), calcular_media())
✔ Laços (while para menu interativo)
✔ Condições (if para validar entradas)

💡 Extras: Armazene as notas em um dicionário com nomes dos alunos e permita ver a média individual.
"""
notas = []

def adicionar_nota():
    print("Digite uma nota: ")
    notas.append(input())

def remover_nota():
    print("Digite a nota que deseja remover: ")
    print(f"Notas digitas: {notas}")
    notas.remove(input())

def calcular_media():
    total = 0
    for n in notas:
        total += float(n)
    print(total / len(notas))

print("Gerenciamento de notas\n")
print("----------------------\n")

opcao = 0

while True:
    print("1 - Adicionar nota")
    print("2 - Remover nota")
    print("3 - Calcular média")
    print("4 - Sair")
    opcao = int(input())
    if opcao == 1:
        adicionar_nota()
    if opcao == 2:
        remover_nota()
    if opcao == 3:
        calcular_media()
    if opcao == 4:
        break
    if opcao > 4:
        print("Opção incorreta!")