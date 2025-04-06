"""
🧠 Desafio: Sistema de Cadastro de Livros
📘 Descrição:
Você precisa criar um pequeno sistema que permita:

Cadastrar livros com título, autor e ano de publicação.
Listar todos os livros cadastrados.
Pesquisar livros por autor.
Remover um livro pelo título.
✅ Regras:
Use classes para representar os livros e o sistema.
Armazene os livros numa lista dentro da classe gerenciadora.
Use métodos para cadastrar, listar, pesquisar e remover.
"""

class Livro:
    def __init__(self, titulo, autor, ano_pupli):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_pupli

    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nAno de publicação: {self.ano_publi}"

    def exibir_livros(self):
        print(f"Titulo: {self.titulo}\nAutor: {self.autor}\nAno de publicação: {self.ano_publi}")

class Biblioteca:
    def __init__(self, livros):
        self.livros = {}

    def adicionar_livro(self,livro):
        if livro.titulo in self.livros:
            print("Livro já cadastrado!")
        else:
            self.livros[livro.titulo] = livro.autor, livro.ano_publi

    def listar_livros(self):
        for livro, (autor, ano) in self.livros.items():
            print(f"{livro} - Autor: {autor}, Ano: {ano}")

livro1 = Livro("Uma Breve História do Tempo", "Stephen Hawking", 1988)
livro2 = Livro("George e o Segredo do Universo", "Christophe Galfard, Lucy Hawking e Stephen Hawking", 2007)



biblioteca = Biblioteca({})
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.listar_livros()

#biblioteca.pesquisar_por_autor("Machado de Assis")
#biblioteca.remover_livro("Dom Casmurro")