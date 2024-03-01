import tkinter as tk
from tkinter import messagebox
from tabla_predictiva import verificar_tabla


def procesar():
    entrada = entry.get()
    resultado = verificar_tabla(entrada)
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, resultado)


root = tk.Tk()
root.title("Tabla predictiva")
root.configure(bg="#f0f0f0")
root.geometry("800x450")

imagen = tk.PhotoImage(file="imagen.png", )
label_imagen = tk.Label(root, image=imagen, bg="#f0f0f0")
label_imagen.grid(row=0, column=0, padx=10, pady=20)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.grid(row=1, column=0, padx=10)

boton_procesar = tk.Button(root, text="Aceptar", command=procesar, font=(
    "Arial", 12), bg="#4CAF50", fg="white")
boton_procesar.grid(row=2, column=0, padx=10, pady=20)

text_area = tk.Text(root, height=20, width=50, font=("Arial", 12))
text_area.grid(row=0, column=1, rowspan=3, padx=10, pady=20)

root.mainloop()
