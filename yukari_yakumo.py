import tkinter as tk
import ran_yakumo as ran
import chen_yakumo as chen
from PIL import Image, ImageTk




class App(tk.Tk):
    def __init__(self, a, b):
        super().__init__()
        self.title('gap youki')
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (a // 2)
        y = (self.winfo_screenheight() // 2) - (b // 2)
        self.geometry(f"{a}x{b}+{x}+{y}")
        self.telaP = TelaPrincipal(self)
        self.telaP.pack(fill='both', expand=True)

#TelaPrincipal extends tk.Frame
class TelaPrincipal(tk.Frame):
    def __init__(self, master):
        super().__init__(master) #super() chama um obj anônimo da classe tk.Frame
        self.config(padx=10, pady=10) #??

        self.frameList = tk.Frame(self)
        self.frameList.pack(fill="both", expand=True)

        # Criando as 3 listas
        self.lista1 = self.createList(self.frameList, "Sites",ran.getKeys('Sites'))
        self.lista2 = self.createList(self.frameList, "Apps",ran.getKeys('Apps'))
        self.lista3 = self.createList(self.frameList, "Archives",ran.getKeys('Archives'))
        self.lista1.pack(side="left", fill="both", expand=True, padx=5)
        self.lista2.pack(side="left", fill="both", expand=True, padx=5)
        self.lista3.pack(side="left", fill="both", expand=True, padx=5)

        self.frameTxt = tk.Frame(self)
        self.frameTxt.pack(fill="x", pady=10)

        self.entrada = tk.Text(self.frameTxt)
        self.entrada.pack(side="left", padx=5)
        self.entrada.focus_set()
        self.entrada.bind("<Tab>", lambda e: self.botaoTxt.focus_set() or "break")

        self.botaoTxt = tk.Button(self.frameTxt, text="Usar Texto")
        self.botaoTxt.pack(padx=5)

        # Carrega imagem
        self.img = ImageTk.PhotoImage(Image.open("img/yukarin.jpg").resize((600, 400)))

        # Canvas
        self.canvas = tk.Canvas(self.frameTxt)
        self.canvas.pack(side="right",fill="both", expand=True)

        # Coloca imagem
        self.canvas.create_image(0, 0, image=self.img)

    def createList(self, parent, titulo, keys):
        frame = tk.LabelFrame(parent, text=titulo)
        container = tk.Frame(frame)
        container.pack(fill="both", expand=True)
        # Palavras como botões clicáveis
        for key in keys:
            btn = tk.Button(container, text=key,
                     command=lambda t=titulo, k=key: ran.openDir(*ran.getValue(t, k)))
            btn.pack(fill="x", pady=2)
        # Botão de adicionar (último elemento da lista)
        tk.Button(container, text="+ Adicionar").pack(fill="x", pady=5)

        return frame

App(900, 500).mainloop()
