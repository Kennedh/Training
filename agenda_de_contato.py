"""
🏆 4. Agenda de Contatos
📌 Objetivo: Criar um sistema de agenda que permita adicionar, remover, buscar e listar contatos armazenados em um dicionário.
🔹 Conceitos usados:
✔ Dicionários ({"nome": "telefone"})
✔ Funções (adicionar_contato(), buscar_contato(), listar_contatos())
✔ Condições (if para verificar se o contato já existe)
✔ Laços (while para menu interativo)
💡 Extras: Permita buscar contatos por parte do nome e salvar os contatos em um arquivo .txt.
"""

agenda = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    numero = input("Digite o número do contato: ")
    agenda[nome] = numero



adicionar_contato()
adicionar_contato()

print(agenda)


