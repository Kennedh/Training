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

        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS tarefas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT,
                    concluida INTEGER,
                    id_usuario INTEGER,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
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

    def inserir_tarefa(self, descricao, id_usuario):
        try:
            self.cursor.execute("INSERT INTO tarefas "
                                    "(descricao, concluida, id_usuario) VALUES (?, ?, ?)",
                           (descricao, 0, id_usuario))
            self.conexao.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as erro:
            return str(erro)

    def valida_login(self,usuario,senha):
        self.cursor.execute("""
        SELECT * FROM usuarios
        WHERE usuario = ? and senha = ?
        """,(usuario, senha))
        resultado = self.cursor.fetchone()
        return resultado

    def buscar_tarefas(self, id_usuario):
        self.cursor.execute("""
        SELECT * FROM tarefas
         WHERE id_usuario = ? 
        """, (id_usuario,))
        tarefas = self.cursor.fetchall()
        return tarefas

    def alterar_status_tarefa(self,novo_status, id_tarefa):
        self.cursor.execute("""
        UPDATE tarefas SET concluida = ? 
        WHERE id = ?
        """,(novo_status, id_tarefa))
        self.conexao.commit()

    def apagar_concluidas(self, id_usuario):
        self.cursor.execute("""
        DELETE FROM tarefas
        WHERE id_usuario = ? and concluida = 1
        """,(id_usuario,))
        self.conexao.commit()

    def apagar_tarefa(self, id_tarefa):
        self.cursor.execute("""
        DELETE FROM tarefas
        WHERE id = ?
        """,(id_tarefa,))
        self.conexao.commit()