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
from datetime import date, datetime, timedelta
import time


pontos = []
menu = """

[1] Registrar Entrada
[2] Registrar Saída
[3] Exibir Resumo do Dia
[4] Sair

"""

print("Bem-vindo ao sistema de controle de ponto!\n")

def registrar_entrada():
    global pontos
    pontos.append(datetime.now())
    print("Registrando entrada...")
    time.sleep(1)
    print("Ponto registrado!")
    time.sleep(1)

def registrar_saida():
    global pontos
    pontos.append(datetime.now())
    print("Registrando saida...")
    time.sleep(1)
    print("Ponto registrado!")
    time.sleep(1)

def resumo_do_dia():
    global pontos
    horas = timedelta()
    print("Gerando resumo do dia...")
    for i in range(0, len(pontos),2):
        horas += pontos[i+1] - pontos[i]
    time.sleep(1)
    for ponto in pontos:
        print(ponto.strftime("%d-%m-%Y %H:%M:%S"))

    horas_trabalhadas = str(horas)
    print(f"Horas trabalhadas {horas_trabalhadas}")
    time.sleep(1)

while True:
    opcao = input(menu)
    if opcao == "1":
        registrar_entrada()
    elif opcao == "2":
        registrar_saida()
    elif opcao == "3":
        resumo_do_dia()
    elif opcao == "4":
        break
    else:
        print("Opção invalida!")




