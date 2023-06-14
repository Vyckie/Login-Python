import customtkinter as ctk
from tkinter import *


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracoesJanelaInicial()
        self.telaLogin()
        
    def configuracoesJanelaInicial(self):
        self.geometry("700x400")
        self.title("Your Finances")
        self.resizable(False, False)
        
    def telaLogin(self):
        
        self.img = PhotoImage(file="Logoo.png")
        self.lbImg = ctk.CTkLabel(self, text=None, image=self.img)
        self.lbImg.grid(row=1, column=0, padx=15, pady=0)
        
        self.title = ctk.CTkLabel(self, text="Faça o seu login ou Cadastre-se\nna nossa plataforma e tenha\n controle total da sua vida financeira!", font=("Century Gothic", 14, "bold"))
        self.title.grid(row=0,column=0, padx=50, pady=20)
        
        self.frameLogin = ctk.CTkFrame(self, width=350, height=380)
        self.frameLogin.place(x=340, y=25)
        
        self.frameTitle = ctk.CTkLabel(self.frameLogin, text="Faça Login", font=("Century Gothic", 22, "bold"))
        self.frameTitle.grid(row=0, column=0, padx=110, pady=30)
        
        self.emailLogin = ctk.CTkEntry(self.frameLogin, width=300, placeholder_text="Digite seu email aqui")
        self.emailLogin.grid(row=1, column=0, padx=10, pady=10)
        
        self.senhaLogin = ctk.CTkEntry(self.frameLogin, width=300, placeholder_text="Digite sua senha aqui", show="*")
        self.senhaLogin.grid(row=2, column=0, padx=10, pady=10)
        
        self.checkboxLogin = ctk.CTkCheckBox(self.frameLogin, text="Manter conectado", checkbox_width=10, checkbox_height=10, corner_radius=20)
        self.checkboxLogin.grid(row=3, column=0, padx=0, pady=20)
        
        self.botaoLogin=ctk.CTkButton(self.frameLogin, width=300, fg_color="#F5F5F5", text_color="#7FC793", text="Logar".upper(), font=("Century Gothic", 12, "bold"))
        self.botaoLogin.grid(row=4, column=0, padx=10, pady=10)
        
        self.botaoCadastro=ctk.CTkButton(self.frameLogin, width=300, text="Cadastre-se".upper(), font=("Century Gothic", 12, "bold"), command=self.telaCadastro)
        self.botaoCadastro.grid(row=5, column=0, padx=10, pady=10)
    
    def telaCadastro(self):
        self.frameLogin.place_forget()
        
        self.frameCadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frameCadastro.place(x=340, y=10)
        
        self.frameTitle = ctk.CTkLabel(self.frameCadastro, text="Faça Seu Cadastro", font=("Century Gothic", 22, "bold"))
        self.frameTitle.grid(row=0, column=0, padx=70, pady=30)
        
        self.nomeCadastro = ctk.CTkEntry(self.frameCadastro, width=300, placeholder_text="Digite seu nome completo aqui")
        self.nomeCadastro.grid(row=1, column=0, padx=10, pady=10)
        
        self.cpfCadastro = ctk.CTkEntry(self.frameCadastro, width=300, placeholder_text="Digite seu CPF aqui")
        self.cpfCadastro.grid(row=2, column=0, padx=10, pady=10)
        
        self.emailCadastro = ctk.CTkEntry(self.frameCadastro, width=300, placeholder_text="Digite seu email aqui")
        self.emailCadastro.grid(row=3, column=0, padx=10, pady=10)
        
        self.senhaCadastro = ctk.CTkEntry(self.frameCadastro, width=300, placeholder_text="Digite sua senha aqui", show="*")
        self.senhaCadastro.grid(row=4, column=0, padx=10, pady=10)
        
        self.senhaConfirmacao = ctk.CTkEntry(self.frameCadastro, width=300, placeholder_text="Digite sua senha novamente", show="*")
        self.senhaConfirmacao.grid(row=5, column=0, padx=10, pady=10)
        
        self.botaoCadastrar=ctk.CTkButton(self.frameCadastro, width=300, text="Cadastrar".upper(), font=("Century Gothic", 12, "bold"), command=self.voltarTelaLogin)
        self.botaoCadastrar.grid(row=6, column=0, padx=10, pady=10)
        
    def voltarTelaLogin(self):
        self.frameCadastro.place_forget()
        self.telaLogin()

    
        
        
        
        
if __name__=="__main__":
    app = App()
    
    app.mainloop()








