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
    agenda[nome.lower()] = numero

def buscar_contato():
    contato = input("Digite o nome para buscar: ")
    consulta = agenda.get(contato, "Contato não encontrado")
    print(consulta)

def listar_contatos():
    print(agenda)

print("""Agenda de contatos
        
        --------------------
        """)

while True:
    print("""1 - Adicionar contato
2 - Buscar contato
3 - Listar contatos
4 - Sair""")
    opcao = int(input())
    if opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        buscar_contato()
    elif opcao == 3:
        listar_contatos()
    elif opcao == 4:
        break
    else:
        print("Opção incorreta!")