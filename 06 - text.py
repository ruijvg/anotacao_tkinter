import tkinter as tk
from tkinter import ttk
cor = "cyan"
root = tk.Tk()
root.geometry("700x700+100+50")
root.config(bg=cor)

style = ttk.Style()
style.configure("My.TButton", font=("arial", 14), background="green")

root.title("Biblioteca Tkinter")

label =  ttk.Label(root, text="Escreve o seu texto aqui...", background=cor, font=("Arial", 15))
label.pack(pady=20, padx=20)

texto = tk.Text(root, width=50, height=20, font=("Arial", 14))
texto.pack()

btn = ttk.Button(root, text="Enviar", style="My.TButton")
btn.pack(pady=10)






root.mainloop()