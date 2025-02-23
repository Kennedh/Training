"""
Desafio: Gerenciador de Tarefas ✅
Crie um programa que funcione como uma lista de tarefas, permitindo ao usuário:

Adicionar uma nova tarefa.
Listar todas as tarefas pendentes.
Marcar uma tarefa como concluída.
Remover uma tarefa.
Sair do programa.
Requisitos
🔹 O programa deve exibir um menu de opções.
🔹 Deve utilizar um dicionário ou lista para armazenar as tarefas.
🔹 As tarefas podem ser representadas por um dicionário, contendo:

Nome da tarefa
Status (pendente ou concluída)
🔹 O programa deve continuar rodando até que o usuário escolha sair.
"""
menu = """
------------MENU----------------
|                              |
| [1] Adicionar uma tarefa     |
| [2] Listar tarefas pendentes |
| [3] Concluir um tarefa       |
| [4] Remover tarefa           |
| [5] Todas as tarefas         |
| [6] Sair                     |
--------------------------------

"""
todas_tarefas = {}

def adicionar_tarefa():
    global todas_tarefas
    tarefa = (input("Digite a tarefa que deseja adicionar\n"))
    todas_tarefas[tarefa] = "Pendente"

def listar_tarefas_pendentes():
    global todas_tarefas
    for tarefa,status in todas_tarefas.items():
        if status == "Pendente":
            print(tarefa)

def concluir_tarefa():
    global todas_tarefas
    print("Qual tarefa deseja concluir:")
    for i, (tarefa, status) in enumerate(todas_tarefas.items(), start=1):
        print(f"{i}. {tarefa} - {status}")
    escolha = int(input())
    tarefa_escolhida = list(todas_tarefas.keys())[escolha - 1]
    todas_tarefas[tarefa_escolhida] = "concluída"

def remover_tarefa():
    global todas_tarefas
    print("Qual tarefa deseja remover:")
    for i, (tarefa, status) in enumerate(todas_tarefas.items(), start=1):
        print(f"{i}. {tarefa} - {status}")
    escolha = int(input())
    tarefa_escolhida = list(todas_tarefas.keys())[escolha - 1]
    todas_tarefas.pop(tarefa_escolhida)

def exibir_todas_tarefas():
    global todas_tarefas
    for tarefa, status in todas_tarefas.items():
        print(f"{tarefa} | {status}")

while True:
    opcao = input(menu)
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas_pendentes()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        exibir_todas_tarefas()
    elif opcao == "6":
        break
    else:
        print("Opção não encontrada!")