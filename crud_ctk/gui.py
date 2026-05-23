import customtkinter as ctk
import banco
from tkinter import messagebox

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class Login(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Tela de Login")
        self.geometry("1024x768")
        self.minsize(600,400)

        # Atributos globais

        self.tarefas = []
        self.id_usuario_logado = None

        # Banco

        self.banco = banco.Banco()

        # ==== Bloco de login =====

        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_login = ctk.CTkLabel(self.frame_login,text="Digite o usuário e senha")
        self.lbl_login.pack(pady=10, padx=20)

        # Campos

        self.campo_user = ctk.CTkEntry(self.frame_login,placeholder_text="Usuário")
        self.campo_user.pack(pady=10, padx=20)

        self.campo_senha = ctk.CTkEntry(self.frame_login, placeholder_text="Senha",show="*")
        self.campo_senha.pack(pady=10, padx=20)

        # botões

        self.btn_entrar = ctk.CTkButton(self.frame_login,text="Entrar", command=self.valida_login)
        self.btn_entrar.pack(pady=10, padx=20)

        self.btn_cadastrar = ctk.CTkButton(self.frame_login, text="Cadastrar",command=self.tela_de_cadastro)
        self.btn_cadastrar.pack(pady=10, padx=20)

        # ==== Bloco de Cadastro ====

        self.frame_cadastro = ctk.CTkFrame(self)

        self.lbl_cadastro = ctk.CTkLabel(self.frame_cadastro, text="Digite as informações do seu usuário")
        self.lbl_cadastro.pack(pady=10, padx=20)

        # Campos

        self.campo_cad_nome = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Nome Completo")
        self.campo_cad_nome.pack(pady=10, padx=20)

        self.campo_cad_email = ctk.CTkEntry(self.frame_cadastro, placeholder_text="E-mail")
        self.campo_cad_email.pack(pady=10, padx=20)

        self.campo_cad_user = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Usuário para entrar")
        self.campo_cad_user.pack(pady=10, padx=20)

        self.campo_cad_senha = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Nova Senha", show="*")
        self.campo_cad_senha.pack(pady=10, padx=20)

        self.campo_conf_senha = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Confime a senha", show="*")
        self.campo_conf_senha.pack(pady=10, padx=20)

        # Botões

        self.btn_salvar_cad = ctk.CTkButton(self.frame_cadastro, text="Salvar Cadastro", command=self.salvar_cadastro)
        self.btn_salvar_cad.pack(pady=10, padx=20)

        self.btn_voltar = ctk.CTkButton(self.frame_cadastro, text="Voltar", command=self.volta_para_login)
        self.btn_voltar.pack(pady=10, padx=20)

        # ==== Bloco do gerenciador de tarefas ====

        self.frame_tarefas = ctk.CTkFrame(self)

        self.lbl_tarefas = ctk.CTkLabel(self.frame_tarefas, text="Tarefas Cadastradas")
        self.lbl_tarefas.pack(pady=10, padx=20)

        self.scroll_tarefas = ctk.CTkScrollableFrame(self.frame_tarefas, width=300, height=200)

        # Campos

        self.campo_tarefa = ctk.CTkEntry(self.frame_tarefas, placeholder_text="Cadastrar novo tarefa")
        self.campo_tarefa.pack(pady=10, padx=20)

        # Frame para os botões

        self.frame_botoes = ctk.CTkFrame(self.frame_tarefas, fg_color="transparent")
        self.frame_botoes.pack(pady=10)

        # Botões

        self.btn_nova_tarefa = ctk.CTkButton(self.frame_botoes, text="Cadastrar", command=self.nova_tarefa)
        self.btn_nova_tarefa.pack(side="left", padx=10)

        self.btn_apagar_concluidas = ctk.CTkButton(self.frame_botoes, text="Apagar Concluídas", command=self.apagar_concluidas)
        self.btn_apagar_concluidas.pack(side="left", padx=10)

    def tela_de_cadastro(self):
        self.frame_login.place_forget()
        self.frame_cadastro.place(relx=0.5, rely=0.5, anchor="center")

    def volta_para_login(self):
        self.frame_cadastro.place_forget()
        self.frame_login.place(relx=0.5, rely=0.5, anchor="center")

    def valida_login(self):
        user = self.campo_user.get()
        password = self.campo_senha.get()

        # Validação no banco

        resultado = self.banco.valida_login(user, password)

        if resultado is None:
            return messagebox.showerror("Erro", "Nome de usuário ou senha incorretos")
        else:
            self.frame_login.place_forget()
            messagebox.showinfo("Sucesso", f"Bem-Vindo {resultado[1]}")
            return self.tela_de_tarefas(resultado[0])

    def salvar_cadastro(self):
        nome = self.campo_cad_nome.get()
        email = self.campo_cad_email.get()
        usuario = self.campo_cad_user.get()
        senha = self.campo_cad_senha.get()
        conf_senha = self.campo_conf_senha.get()

        if senha != conf_senha:
             return messagebox.showerror("Erro", "Senhas não coincidem!")

        resultado = self.banco.inserir_usuario(nome,email,usuario,senha)

        if resultado == "Usuário Cadastrado":
            messagebox.showinfo("Sucesso", resultado)
            self.frame_cadastro.place_forget()
            self.frame_login.place(relx=0.5, rely=0.5, anchor="center")
        else:
            messagebox.showerror("Erro", resultado)

    def tela_de_tarefas(self,id_usuario):
        self.id_usuario_logado = id_usuario
        self.tarefas = self.banco.buscar_tarefas(id_usuario)

        self.scroll_tarefas.pack(pady=10, padx=20)

        for tarefa in self.tarefas:
            # Frame para cada linha pois o ctk se perde tadinho

            frame_linhas = ctk.CTkFrame(self.scroll_tarefas, fg_color="transparent")
            frame_linhas.pack(fill="x", pady=5)

            checkbox_tarefa = ctk.CTkCheckBox(frame_linhas, text=f"{tarefa[1]}")
            checkbox_tarefa.configure(
                command=lambda t_id=tarefa[0], check=checkbox_tarefa: self.clique_check_box(t_id, check))
            checkbox_tarefa.pack(side="left", pady=5)

            btn_apagar = ctk.CTkButton(frame_linhas, text="Apagar",  width=50)
            btn_apagar.configure(command=lambda id_tarefa=tarefa[0]: self.apagar_tarefa(id_tarefa))
            btn_apagar.pack(side="right", pady=5)

            if tarefa[2] == 1:
                checkbox_tarefa.select()

        self.frame_tarefas.place(relx=0.5, rely=0.5, anchor="center")

    def nova_tarefa(self):
        tarefa = self.campo_tarefa.get()
        self.banco.inserir_tarefa(tarefa,self.id_usuario_logado)

        for widget in self.scroll_tarefas.winfo_children():
            widget.destroy()

        self.campo_tarefa.delete(0, 'end')
        self.tela_de_tarefas(self.id_usuario_logado)

        return messagebox.showinfo("Sucesso","Nova Tarefa cadastrada")

    def clique_check_box(self,id_tarefa, checkbox_clicado):
        novo_status = checkbox_clicado.get()
        self.banco.alterar_status_tarefa(novo_status, id_tarefa)

    def apagar_concluidas(self):
        self.banco.apagar_concluidas(self.id_usuario_logado)

        for widget in self.scroll_tarefas.winfo_children():
            widget.destroy()

        self.tela_de_tarefas(self.id_usuario_logado)

        return messagebox.showinfo("Sucesso", "Tarefas concluídas foram apagadas :-)")

    def apagar_tarefa(self, id_tarefa):
        self.banco.apagar_tarefa(id_tarefa)

        for widget in self.scroll_tarefas.winfo_children():
            widget.destroy()

        self.tela_de_tarefas(self.id_usuario_logado)

        return messagebox.showinfo("Sucesso", "Tarefas apagada")