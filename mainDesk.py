import tkinter as tk
from tkinter import ttk, messagebox
import ctypes


lib = ctypes.CDLL("./funcao.dll")
lib.verificar_login.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.verificar_login.restype = ctypes.c_int

def verificar_login(usuario, senha):
    u = usuario.encode("utf-8")
    s = senha.encode("utf-8")
    return lib.verificar_login(u, s) == 1

lib.cadastro_usuario.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.cadastro_usuario.restype = ctypes.c_int

def cadastro_usuario(usuario, senha):
    return lib.cadastro_usuario(usuario.encode(), senha.encode()) == 1




class TelaLogin(tk.Tk): # ------------------------------------------------------------------------------Login
    def __init__(self):
        super().__init__()
        self.title("Studium")
        self.geometry("420x420")
        self.configure(bg="#e8f0fe")
        self.resizable(False, False)

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("TFrame", background="#ffffff")
        estilo.configure("TLabel", background="#ffffff", foreground="#333", font=("Segoe UI", 10))
        estilo.configure("TEntry", padding=5)
        estilo.configure("TButton", background="#4a90e2", foreground="white", font=("Segoe UI", 10, "bold")) # -----------------Cuidado botao zuado
        estilo.map("TButton",background=[("active", "#357ABD")],foreground=[("active", "white")])

    
        frame = ttk.Frame(self)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=300)

        fundo = tk.Frame(frame, bg="#ffffff")
        fundo.pack(fill="both", expand=True)

        tk.Label(fundo, text="Acesse sua conta", font=("Segoe UI", 14, "bold"), bg="#ffffff", fg="#333").pack(pady=(20, 10))

        ttk.Label(fundo, text="Usuário").pack(anchor="w", padx=30)
        self.entrada_usuario = ttk.Entry(fundo, width=30)
        self.entrada_usuario.pack(pady=5)

        ttk.Label(fundo, text="Senha").pack(anchor="w", padx=30)
        self.entrada_senha = ttk.Entry(fundo, show="*", width=30)
        self.entrada_senha.pack(pady=5)

        botao_login = ttk.Button(fundo, text="Entrar",  command=self.verificar)
        botao_login.pack(pady=15)

        ir_cadastro = ttk.Button(fundo, text="Cadastrar",  command=self.cadastro_tela)
        ir_cadastro.pack()

    def cadastro_tela(self):
        CadastroTela()

    def verificar(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()
        if verificar_login(usuario, senha):
            messagebox.showinfo("Login", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

class CadastroTela(tk.Toplevel): #--------------------------------------------------------------------------------------------------------Segunda Tela - Cadastro
    def __init__(self):
        super().__init__()
        self.title("Studium - Cadastro")
        self.geometry("420x320")
        self.configure(bg="#e8f0fe")
        self.resizable(False, False)
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("TFrame", background="#ffffff")
        estilo.configure("TLabel", background="#ffffff", foreground="#333", font=("Segoe UI", 10))
        estilo.configure("TEntry", padding=5)
        estilo.configure("TButton", background="#4a90e2", foreground="white", font=("Segoe UI", 10, "bold")) # -----------------Cuidado botao zuado
        estilo.map("TButton",background=[("active", "#357ABD")],foreground=[("active", "white")])

        frame = ttk.Frame(self)
        frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=260)

        fundo = tk.Frame(frame, bg="#ffffff")
        fundo.pack(fill="both", expand=True)

        ttk.Label(fundo, text="Usuário").pack(anchor="w", padx=30)
        self.entrada_usuario = ttk.Entry(fundo, width=30)
        self.entrada_usuario.pack(pady=5)

        ttk.Label(fundo, text="Senha").pack(anchor="w", padx=30)
        self.entrada_senha = ttk.Entry(fundo, show="*", width=30)
        self.entrada_senha.pack(pady=5)

        ttk.Label(fundo, text="Confirme sua Senha").pack(anchor="w", padx=30)
        self.Confirma_senha = ttk.Entry(fundo, show="*", width=30)
        self.Confirma_senha.pack(pady=5)

        botao_login = ttk.Button(fundo, text="Cadastrar",  command=self.verifica_senha)
        botao_login.pack(pady=15)

    
    def verifica_senha(self):
        self.nome = self.entrada_usuario.get()
        self.senha = self.entrada_senha.get()
        self.senhaConfirm = self.Confirma_senha.get()

        if self.senha == self.senhaConfirm:
            if cadastro_usuario(self.nome, self.senha):
                messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
                self.destroy()
        else:
            messagebox.showerror("Erro", "Senhas não compátiveis.")
if __name__ == "__main__":
    app = TelaLogin()
    app.mainloop()