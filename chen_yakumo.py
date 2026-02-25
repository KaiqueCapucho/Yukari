import tkinter as tk
import ran_yakumo as ran

def openTelaAdd(self, titulo):
    newWindow = tk.Toplevel(self.master)
    newWindow.title("Tela de Adição")
    newWindow.geometry("300x350")
    TelaAdd(newWindow, titulo)



class TelaAdd(tk.Frame):
    def __init__(self, master, titulo):
        super().__init__(master)
        self.pack(padx=20, pady=20)

        # Título opcional
        self.title = tk.Label(self, text="Adicionar Dados", font=("Arial", 14))
        self.title.pack(pady=10)
        self.titulo = titulo
        key,value,note = ran.getColumns(titulo)

        # Chave
        tk.Label(self, text=key).pack(anchor="w")
        self.chave = tk.Entry(self, width=30)
        self.chave.pack(pady=5)

        # Value
        tk.Label(self, text=value).pack(anchor="w")
        self.valor = tk.Entry(self, width=30)
        self.valor.pack(pady=5)

        # Nota
        tk.Label(self, text=note).pack(anchor="w")
        self.nota = tk.Entry(self, width=30)
        self.nota.pack(pady=5)

        # Frame para os botões
        self.frame_botoes = tk.Frame(self)
        self.frame_botoes.pack(pady=15)

        # Botão Confirmar (sem comando/back-end)
        self.btnCancela = tk.Button(self.frame_botoes, text="Cancelar",
                                    command= lambda: self.btnCancelar())
        self.btnCancela.pack(side="left", padx=5)

        # Botão Cancelar (sem comando/back-end)
        self.btnConfirma = tk.Button(self.frame_botoes, text="Confirmar",
                             command= lambda: self.btnConfirmar())
        self.btnConfirma.pack(side="left", padx=5)

    def btnCancelar(self):
        a = 1

    def btnConfirmar(self):
        ran.insertValue(self.titulo, self.chave.get(), self.valor.get(), int(self.nota.get()) )
        #fechar tela