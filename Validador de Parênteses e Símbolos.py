"""
Imagine que você está construindo um compilador ou um editor de texto (como o VS Code).
Você precisa criar uma função que verifique se a abertura e o fechamento de símbolos em uma expressão matemática ou
código estão corretos e na ordem certa.Símbolos permitidos: (), [], {}.Regras: todo símbolo aberto deve ser fechado
pelo seu par correspondente.Um símbolo deve ser fechado na ordem inversa em que foi aberto (LIFO - Last In, First Out).
A função deve retornar True se a sequência for válida e False caso contrário.
Exemplos de Entrada e Saída:

Entrada,Saída Esperada,Motivo
"{[()]}",True,Tudo fechado na ordem correta.
"{[(])}",False,O ] tentou fechar o ( (ordem errada).
"{{[",False,Abriu símbolos que nunca foram fechados.
")(",False,Começou fechando algo que não estava aberto.

"""


def valida_exp(texto):
    temp = []
    abre = ["{", "[", "("]
    pares = {')': '(', ']': '[', '}': '{'}

    if not texto or texto[0] in pares:
        return False

    for simbol in texto:
        if simbol in abre:
            temp.append(simbol)
        elif simbol in pares:
            if temp:
                ultimo = temp.pop()
                if pares[simbol] != ultimo:
                    return False
            else:
                return False
    return len(temp) == 0


print(valida_exp("{[()]}"))
print(valida_exp("{[(])}"))
print(valida_exp("{{["))
print(valida_exp(")("))
