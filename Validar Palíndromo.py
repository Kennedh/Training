"""
Uma frase é um palíndromo se, após remover todos os caracteres não alfanuméricos (espaços, pontuação) e converter tudo
para minúsculas, ela for lida da mesma forma de frente para trás e de trás para frente.
"""


def eh_palindromo(s):
    s_limpa = ''.join(char for char in s if char.isalnum()).lower()
    left = 0
    right = len(s_limpa) - 1
    while left < right:
        if s_limpa[left] == s_limpa[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

# --- TESTES ---
testes = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("Arara", True),
    ("12321", True)
]

for texto, esperado in testes:
    print(f"'{texto}' -> {eh_palindromo(texto)} (Esperado: {esperado})")