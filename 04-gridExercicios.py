import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.title("Africa Cuidado com a China")
root.geometry("600x600")

style = ttk.Style()
style.theme_use('classic')  # Opções: 'default', 'classic', 'clam', 'alt'

lbl_nome = ttk.Label(root, text="Nome: ", font=("Arial, 14"))
lbl_nome.grid(row=20, column=20, pady=20, padx=30)

entrada = ttk.Entry(root, width=40)
entrada.grid(row=20, column=21, pady=20, padx=30)

lbl_apelido = ttk.Label(root, text="Apelido: ", font=("Arial, 14"))
lbl_apelido.grid(row=30, column=20, pady=20, padx=30)

entrada_apelido = ttk.Entry(root, width=40)
entrada_apelido.grid(row=30, column=21, pady=20, padx=30)

btn_ok = ttk.Button(root, text="ok")
btn_ok.grid(row=40, column=21, padx=20, pady=20)

btn_cancel = ttk.Button(root, text="Cancelar")
btn_cancel.grid(row=40, column=22, padx=20, pady=20)







root.mainloop()