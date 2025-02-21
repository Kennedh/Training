"""🏆 5. Jogo de Pedra, Papel e Tesoura com Placar
📌 Objetivo: Criar um jogo interativo onde o usuário joga contra o computador e um placar registra as vitórias.
🔹 Conceitos usados:
✔ Funções (escolha_computador(), verificar_vencedor())
✔ Repetição (while para jogar várias rodadas)
✔ Condições (if para validar a escolha do jogador)
✔ Biblioteca random para escolher jogada do computador
💡 Extras: Adicione um modo Melhor de 3 e um sistema de níveis de dificuldade (aleatório ou "inteligente" baseado em padrões).
"""

import random

def escolha_computador():
    op = ["pedra", "papel", "tesoura"]
    escolha = random.choice(op)
    return escolha

def verificar_vencedor(valor2):
    valor1 = escolha_computador()

    print(f"\nO computador escolheu {valor1}\n")

    if (valor1 == "pedra" and valor2 == "tesoura") or \
        (valor1 == "papel" and valor2 == "pedra") or \
        (valor1 == "tesoura" and valor2 == "papel"):
        print("Computador ganhou!")
    elif valor1 == valor2:
        print("Empate!")
    elif valor2 != "pedra" or "papel" or "tesoura":
        print("Escolha incorreta")
    else:
        print("Você ganhou!")

while True:
    escolha_usuario = input("\nEscolha entre pedra, papel ou tesoura\n").lower()
    if escolha_usuario == "sair":
        break
    verificar_vencedor(escolha_usuario)