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
    f = False
    temp = []
    abre = ["{","[","("]
    fecha = ["}","]",")"]
    pares = {')': '(', ']': '[', '}': '{'}
    if texto[0] not in abre:
        return False
    for simbol in texto:
        if simbol in abre and f:
            temp.append(simbol)
        else:
            if temp:
                ultimo = temp[len(temp) - 1]
            else:
                break
            f = True
            if pares.get(simbol) == ultimo:
                temp.pop()
            else:
                return False
    return True


print(valida_exp("{[()]}"))
print(valida_exp("{[(])}"))
print(valida_exp("{{["))
print(valida_exp(")("))
