import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.config(background="black")
root.geometry("720x720+50+50")
root.title("Zonas da Vila de Achada Do Monte.")

lbl1 = ttk.Label(root, text = "Achadona", background = "violet", foreground="black", font = ("Arial, 20"))
lbl1.pack(side = "top")

lbl2 = ttk.Label(root, text = "Meio de Achada", background = "green", foreground ="white", font = ("Arial, 20"))
lbl2.pack(side = "right", fill="x")

lbl3 = ttk.Label(root, text ="Palha Carga", font =("Arial, 25"), background="yellow", foreground="green")
lbl3.pack(side="left", fill="x")

lbl4 = ttk.Label(root, text="Manguinho", font = ("Arial, 20"), background="blue", foreground="white")
lbl4.pack(side="bottom")



root.mainloop()