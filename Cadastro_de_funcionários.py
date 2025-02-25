"""
📌 Desafio: Cadastro de Funcionários
Crie um programa que gerencie o cadastro de funcionários de uma empresa. O programa deve permitir adicionar funcionários e exibir um relatório com os dados cadastrados.

Requisitos:
Crie uma função chamada adicionar_funcionario(nome, idade, cargo, salario), que recebe essas informações e armazena os funcionários em uma lista de dicionários.
Crie outra função chamada exibir_relatorio(), que exibe a lista de funcionários cadastrados de forma organizada.
Permita que o usuário adicione vários funcionários e depois visualize o relatório.
"""

menu = """

 Cadastro de Funcionários 
-----------------------------------------
[1] Adicionar Funcionário
[2] Remover Funcionário
[3] Relatorio de funcionários cadastrados
[4] Sair
------------------------------------------
"""
relatorio = ""
lista = []
num_funcionarios = 0

def adicionar_funcionario():
    global relatorio
    global num_funcionarios
    dicio = {}
    global lista
    num_funcionarios += 1
    nome = input("Nome do funcionário: ")
    dicio["Nome"] = nome
    idade = input("Idade: ")
    dicio["Idade"] = idade
    cargo = input("Cargo: ")
    dicio["Cargo"] = cargo
    salario = input("Salário: ")
    dicio["Salário"] = f"R$ {salario}"
    print("\nFuncionário cadastrado com sucesso!")
    lista.append(dicio)

def exibir_relatorio():
    global relatorio
    global num_funcionarios
    global lista
    print("Lista de Funcionários:")
    print("----------------------")
    for idx, item in enumerate(lista):
        print(f"Código: {idx+1}"+"".join(f" | {chave}: {valor}" for chave, valor in item.items()))
    print("----------------------")
    print(f"Total de funcionários cadastrados: {len(lista)}")

def remover_funcionario():
    global lista
    global num_funcionarios
    op = int(input("Digite o código do funcionário que deseja excluir: "))
    lista.pop(op-1)
    num_funcionarios -= 1

while True:
    opcao = input(menu)
    if opcao == "1":
        adicionar_funcionario()
    elif opcao == "2":
        remover_funcionario()
    elif opcao == "3":
        exibir_relatorio()
    elif opcao == "4":
        break
    else:
        print("Opção incorreta!")