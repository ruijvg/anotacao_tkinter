import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("São Miguel")
root.geometry("500x500")

lbl_1 = ttk.Label(root, text="Apresentação do Município")
lbl_1.grid(row=10, column=30, pady=50, padx=50)

btn_1 = ttk.Button(root, text = "Norte")
btn_1.grid(row=50, column=20, pady=20, padx=30)

btn_2 = ttk.Button(root, text = "Sul")
btn_2.grid(row=50, column=21, pady=20, padx=30)





root.mainloop()