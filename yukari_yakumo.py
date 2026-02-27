import tkinter as tk
import ran_yakumo as ran
from chen_yakumo import openTelaAdd
from PIL import Image, ImageTk



def createList(parent, titulo:str, keys:list[str]):
    frame = tk.LabelFrame(parent, text=titulo)
    container = tk.Frame(frame)
    container.pack(fill="both", expand=True)
    for key in keys:
        tk.Button(container, text=key,
           command=lambda t=titulo, k=key: btnListOnClick(parent,t,k)).pack(fill="x", pady=2)

    tk.Button(container, text="+ Add", command=lambda:openTelaAdd(parent, titulo)
              ).pack(fill="x", pady=5)
    return frame

def btnListOnClick(parent:tk, table:str, key:str):
    ran.openDir(ran.getValue(table, key))
    parent.winfo_toplevel().destroy()

######
def btnTxtOnClick(master, txt):
    for t in txt.strip().splitlines():
        if t in ran.getKeys('Sites'):    ran.openDir(ran.getValue('Sites', t))
        if t in ran.getKeys('Apps'):     ran.openDir(ran.getValue('Apss', t))
        if t in ran.getKeys('Archives'): ran.openDir(ran.getValue('Archives', t))

    master.destroy()

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

        self.sites = createList(self.frameList, "Sites",    ran.getKeys('Sites'))
        self.sites.pack(side="left", fill="both", expand=True, padx=5)

        self.apps = createList(self.frameList, "Apps",     ran.getKeys('Apps'))
        self.apps.pack(side="left", fill="both", expand=True, padx=5)

        self.archs = createList(self.frameList, "Archives", ran.getKeys('Archives'))
        self.archs.pack(side="left", fill="both", expand=True, padx=5)


        self.frameTxt = tk.Frame(self)
        self.frameTxt.pack(fill="x", pady=10)

        self.entrada = tk.Text(self.frameTxt)
        self.entrada.pack(side="left", padx=5)
        self.entrada.focus_set()
        self.entrada.bind("<Tab>", lambda e: self.botaoTxt.focus_set() or "break")

        self.botaoTxt = tk.Button(self.frameTxt, text="Procurar", command=lambda: btnTxtOnClick(master, self.entrada.get("1.0",tk.END)))
        self.botaoTxt.pack(padx=5)

        # Carrega imagem
        #self.img = ImageTk.PhotoImage(Image.open("img/yukarin.jpg").resize((600, 400)))

        # Canvas
        #self.canvas = tk.Canvas(self.frameTxt)
        #self.canvas.pack(side="right",fill="both", expand=True)

        # Coloca imagem
        #self.canvas.create_image(0, 0, image=self.img)


App(900, 500).mainloop()
