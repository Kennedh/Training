import random

def obter_escolha_computador():
    """Retorna a escolha aleatória do computador."""
    return random.choice(["pedra", "papel", "tesoura"])

def verificar_vencedor(jogador, computador):
    """
    Compara as jogadas e retorna o vencedor.
    Usamos um dicionário onde a chave é a jogada e o valor é o que ela derrota.
    """
    vence_de = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }

    if jogador == computador:
        return "empate"
    elif vence_de[jogador] == computador:
        return "jogador"
    else:
        return "computador"

def jogar():
    placar_jogador = 0
    placar_computador = 0
    opcoes_validas = ["pedra", "papel", "tesoura"]

    print(" Bem-vindo ao Jogo de Pedra, Papel e Tesoura! 🏆")
    print("Digite 'sair' a qualquer momento para encerrar o jogo.\n")

    while True:
        # Pega a escolha, remove espaços extras e passa para minúsculo
        escolha_usuario = input("Sua escolha (pedra, papel, tesoura): ").strip().lower()

        # Condição de saída
        if escolha_usuario == "sair":
            print("\n Jogo encerrado!")
            print(f" PLACAR FINAL -> Você: {placar_jogador} | Computador: {placar_computador}")
            break

        # Validação da entrada (substitui o seu antigo elif)
        if escolha_usuario not in opcoes_validas:
            print(" Escolha inválida. Tente novamente!\n")
            continue

        # Ações do jogo
        escolha_comp = obter_escolha_computador()
        print(f" O computador escolheu: {escolha_comp}")

        # Verificação
        resultado = verificar_vencedor(escolha_usuario, escolha_comp)

        # Atualização do placar e feedback
        if resultado == "jogador":
            print(" Você ganhou esta rodada!\n")
            placar_jogador += 1
        elif resultado == "computador":
            print(" O computador ganhou esta rodada!\n")
            placar_computador += 1
        else:
            print(" Deu empate!\n")

        print(f" Placar Atual -> Você: {placar_jogador} | Computador: {placar_computador}\n")
        print("-" * 40)

# Inicia o programa
if __name__ == "__main__":
    jogar()
