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
| [5] Sair                     |
--------------------------------

"""

def adicionar_tarefa():
    pass

def listar_tarefas_pendentes():
    pass

def concluir_tarefa():
    pass

def remover_tarefa():
    pass

while True:
    opcao = int(input(menu))
    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        listar_tarefas_pendentes()
    elif opcao == 3:
        concluir_tarefa()
    elif opcao == 4:
        remover_tarefa()
    elif opcao == 5:
        break
    else:
        print("Opção não encontrada!")