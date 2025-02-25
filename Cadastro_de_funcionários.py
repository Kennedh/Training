"""
📌 Desafio: Cadastro de Funcionários
Crie um programa que gerencie o cadastro de funcionários de uma empresa. O programa deve permitir adicionar funcionários e exibir um relatório com os dados cadastrados.

Requisitos:
Crie uma função chamada adicionar_funcionario(nome, idade, cargo, salario), que recebe essas informações e armazena os funcionários em uma lista de dicionários.
Crie outra função chamada exibir_relatorio(), que exibe a lista de funcionários cadastrados de forma organizada.
Permita que o usuário adicione vários funcionários e depois visualize o relatório.
"""

funcionarios = ""
num_funcionarios = 0

def adicionar_funcionario(nome, idade, cargo, salario):
    global funcionarios
    global num_funcionarios
    num_funcionarios += 1
    funcionarios += f"Nome: {nome} | Idade: {idade} | Cargo: {cargo} | Salário: R$ {salario}\n"

def exibir_relatorio():
    global funcionarios
    global num_funcionarios
    print("Lista de Funcionários:")
    print("----------------------")
    print(funcionarios)
    print("----------------------")
    print(f"Total de funcionários cadastrados: {num_funcionarios}")



adicionar_funcionario("Carlos", 30, "Analista", 4500)
adicionar_funcionario("Ana", 25, "Desenvolvedora", 5500)
adicionar_funcionario("Marcos", 40, "Gerente", 7500)

exibir_relatorio()