import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class Login(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Tela de Login")
        self.geometry("1200x750")
        self.minsize(600,400)

        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_login = ctk.CTkLabel(self.frame_login,text="Digite o usuário e senha")
        self.lbl_login.pack(pady=10, padx=20)

        self.campo_user = ctk.CTkEntry(self.frame_login)
        self.campo_user.pack(pady=10, padx=20)

        self.campo_senha = ctk.CTkEntry(self.frame_login,show="*")
        self.campo_senha.pack(pady=10, padx=20)

        self.btn_entrar = ctk.CTkButton(self.frame_login,text="Entrar")
        self.btn_entrar.pack(pady=10, padx=20)

        self.btn_cadastrar = ctk.CTkButton(self.frame_login, text="Cadastrar")
        self.btn_cadastrar.pack(pady=10, padx=20)