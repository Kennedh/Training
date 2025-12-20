"""
Imagine que você está criando um editor de texto simplificado. Você precisa implementar duas funções:

Escrever: Adiciona um texto ao documento.

Desfazer (Undo): Remove a última alteração e a guarda em uma "memória temporária".

Refazer (Redo): Pega a última ação desfeita e a coloca de volta no documento.

Para isso, você usará duas pilhas: uma para o histórico de ações e outra para o que foi desfeito.

O que você deve implementar:
Crie uma classe ou um conjunto de funções que gerencie uma lista de strings.

escrever(texto): Adiciona a string à lista.

desfazer(): Tira o último item da lista de texto e coloca na lista de "refazer".

refazer(): Tira o último item da lista de "refazer" e coloca de volta na lista de texto.

Exemplo de Fluxo:
escrever("Olá") -> Documento: ["Olá"]

escrever("Mundo") -> Documento: ["Olá", "Mundo"]

desfazer() -> Documento: ["Olá"] (O "Mundo" foi para a pilha de refazer)

refazer() -> Documento: ["Olá", "Mundo"]
"""

historico = []
refazer_pilha = []


def escrever(texto):
    historico.append(texto)
    refazer_pilha.clear()
    print(f"Documento atual: {" ".join(historico)}")


def desfazer():
    if not historico:
        print("Nada para desfazer.")
        return
    refazer_pilha.append(historico[-1])
    historico.pop()
    print(f"Documento após desfazer: {" ".join(historico)}")


def refazer():
    if not refazer_pilha:
        print("Nada para refazer.")
        return

    historico.append(refazer_pilha[-1])
    refazer_pilha.pop()
    print(f"Documento após refazer: {" ".join(historico)}")


# Teste

escrever("Python")
escrever("é")
escrever("legal")
desfazer()
refazer()