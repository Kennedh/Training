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

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Teste

trie = Trie()
trie.insert("casa")
trie.insert("casamento")

print(trie.search("casa"))
print(trie.search("cas"))
print(trie.starts_with("cas"))
print(trie.starts_with("casa"))
print(trie.starts_with("casamen"))
print(trie.starts_with("casar"))