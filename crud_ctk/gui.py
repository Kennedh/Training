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

        # Banco

        self.banco = banco.Banco()

        # Bloco de login

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

        # Bloco de Cadastro

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
            return messagebox.showinfo("Sucesso", f"Bem-Vindo {resultado[1]}")

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