"""
Uma Trie é uma estrutura de árvore digital usada para armazenar um conjunto dinâmico de strings, onde as chaves
geralmente são strings. Ela é extremamente eficiente para buscas do tipo "começa com".

O que você precisa codificar:
Você deve criar uma classe Trie com os seguintes métodos:

insert(word): Insere uma string na estrutura.

search(word): Retorna True se a palavra exata estiver na Trie.

starts_with(prefix): Retorna True se houver alguma palavra inserida que comece com esse prefixo.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        pass

    def search(self, word: str):
        pass

    def starts_with(self, prefix: str):
        pass