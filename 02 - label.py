import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Ponta Manguinho")
janela.geometry("500x500+100+200")

lbl_nome = ttk.Label(janela, text="Zona de Marias", foreground="red", font=("Arial, 20"), background="green")
lbl_nome.pack(side="bottom", fill="y", padx=50, pady=100)  #side = top, bottom   #fill = x, y




janela.mainloop()


"""
✅ Opções de side:

Valor	Significado
"top"	Coloca o widget no topo (padrão)
"bottom"	Coloca o widget na parte inferior
"left"	Alinha o widget à esquerda
"right"	Alinha o widget à direita

"""