import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("O meu estilo de Botão")
root.geometry("500x500")


style = ttk.Style()
style.configure("Btn.TButton", font=("Arial",12),foreground="blue",background="green" )
style.configure("Btn2.TButton", font=("Helvetica", 12), foreground="red",background="yellow")
style.configure("Lbl1.TLabel", font=("Helvetica", 20), foreground="red",background="black")


lbl_nome = ttk.Label(root, text="Nome de Utilizador: ", style="Lbl1.TLabel")
lbl_nome.pack()
botao = ttk.Button(root, text="Botão de ação", style="Btn.TButton")
botao.pack()

botao2 = ttk.Button(root, text="Botao de segunda", style="Btn2.TButton")
botao2.pack()






root.mainloop()