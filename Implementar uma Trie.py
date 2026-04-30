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
    __slots__ = ('children', 'is_end_of_word')
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    __slots__ = ('root',)
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # Usa setdefault para evitar dupla verificação
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word: str) -> bool:
        """Remove uma palavra da Trie (opcional)"""
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            
            char = word[depth]
            if char not in node.children:
                return False
            
            should_delete = _delete(node.children[char], word, depth + 1)
            
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        return _delete(self.root, word, 0)

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
