"""
Você tem uma lista de preços onde precos[i] é o preço de uma ação no dia i. Você quer maximizar seu lucro escolhendo um
único dia para comprar e um dia diferente no futuro para vender.

Retorne o lucro máximo que você pode obter. Se não der para ter lucro nenhum, retorne 0.

Regra de Ouro: Você não pode vender antes de comprar (obviamente, a gente não viaja no tempo... ainda).
"""


def max_lucro(precos):
    if len(precos) < 2:
        return 0
    menor_preco = precos[0]
    melhor_lucro = 0
    for num in precos:
        if num < menor_preco:
            menor_preco = num
        lucro_atual = num - menor_preco
        if lucro_atual > melhor_lucro:
            melhor_lucro = num - menor_preco
    return melhor_lucro


# --- TESTES ---
testes = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2], 1),
    ([2, 4, 1], 2),  # Compra 2, vende 4. Ignora o 1 pq ele aparece depois da venda.
    ([2, 1, 2, 0, 1], 1)
]

print(f"{'PREÇOS':<20} | {'ESPERADO':<10} | {'RESULTADO':<10} | {'STATUS'}")
print("-" * 60)

todos_passaram = True
for lista, esperado in testes:
    resultado = max_lucro(lista)
    status = "✅" if resultado == esperado else "❌"
    if resultado != esperado: todos_passaram = False

    print(f"{str(lista):<20} | {str(esperado):<10} | {str(resultado):<10} | {status}")

if todos_passaram:
    print("\n🚀 O Lobo de Wall Street! Acertou tudo.")
else:
    print("\n📉 O mercado quebrou. Tente rever a lógica.")

teste = [7, 1, 5, 3, 6, 4]

