import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect("aplicativo.db")
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT UNIQUE,
            usuario TEXT UNIQUE,
            senha text
        )""")

    def inserir_usuario(self, nome, email, usuario, senha):
        try:
            self.cursor.execute("INSERT INTO usuarios "
                                    "(nome, email, usuario, senha) VALUES (?, ?, ?, ?)",
                           (nome, email, usuario, senha))
            self.conexao.commit()
            return "Usuário Cadastrado"
        except sqlite3.IntegrityError as erro:
            msg_error = str(erro)
            if "usuario" in msg_error:
                return "Este usuário já está cadastrado!"
            if "email" in msg_error:
                return "Este e-mail já está cadastrado!"