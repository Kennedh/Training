"""
Você deve escrever uma função que recebe duas strings e verifica se elas são anagramas uma da outra. Duas palavras são
anagramas se forem formadas exatamente pelas mesmas letras, na mesma quantidade, apenas em ordem diferente.
"""

def sao_anagramas(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    s1 = list(s1)
    s2 = list(s2)

    for letra in s1:
        if letra in s2:
            s2.remove(letra)
        else:
            return False
    if not s2:
        return True
    else:
        return False

# Teste

# Testador feito pelo Gemini 3

def rodar_testes():
    casos_de_teste = [
        ("amor", "roma", True),
        ("Iracema", "America", True),
        ("Estuda", "Duates", True),
        ("banana", "nabana", True),
        ("carro", "cora", False),  # Faltou um 'r'
        ("pato", "sapo", False),  # Letras diferentes
        ("Listen", "Silent", True),
        ("A dama admirou o rímel", "O milagre da alma ruiu", False),  # Frase longa
        ("The eyes", "They see", True)  # Frase com espaços
    ]

    print(f"{'ENTRADA 1':<15} | {'ENTRADA 2':<15} | {'ESPERADO':<10} | {'RESULTADO':<10}")
    print("-" * 65)

    todos_passaram = True

    for s1, s2, esperado in casos_de_teste:
        resultado = sao_anagramas(s1, s2)
        status = "✅" if resultado == esperado else "❌"

        if resultado != esperado:
            todos_passaram = False

        # Formata para não quebrar a tabela visualmente
        p1 = (s1[:12] + '..') if len(s1) > 12 else s1
        p2 = (s2[:12] + '..') if len(s2) > 12 else s2

        print(f"{p1:<15} | {p2:<15} | {str(esperado):<10} | {status} {resultado}")

    print("-" * 65)
    if todos_passaram:
        print("🏆 Perfeito! O detetive desvendou todos os casos.")
    else:
        print("⚠️ Ops! Algo não bateu. Verifique a lógica de contagem.")


if __name__ == "__main__":
    rodar_testes()