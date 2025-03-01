"""
📌 Desafio: Controle de Ponto dos Funcionários
Crie um programa que simule um controle de ponto para funcionários. O sistema deve registrar os horários de entrada e saída e calcular o tempo total trabalhado no dia.

📌 Requisitos:
Registrar o horário de entrada quando o funcionário iniciar o expediente.
Registrar o horário de saída quando o funcionário encerrar o expediente.
Calcular a duração total do expediente e exibir no formato HH:MM:SS.
O sistema deve permitir múltiplas entradas e saídas no mesmo dia (ex: para considerar horário de almoço).
Ao final do expediente, o programa deve exibir um resumo do dia, incluindo o tempo total trabalhado.
"""
import sys

menu = """

[1] Registrar Entrada
[2] Registrar Saída
[3] Exibir Resumo do Dia
[4] Sair

"""

print("Bem-vindo ao sistema de controle de ponto!\n")

def registrar_entrada():
    pass

def registrar_saida():
    pass

def calcular_total_trabalhado():
    pass

while True:
    horario = input("Digite a hora no formato HH:MM → ")
    if len(horario) == 5 and horario[2] == ":" and horario[:2].isdigit() and horario[3:].isdigit():
        break
    print("Formato inválido! Use HH:MM.")

print(f"Horário registrado: {horario}")