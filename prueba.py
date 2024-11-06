import tkinter as tk
from tkinter import messagebox

CONVERSION_GALONES_A_LITROS = 3.78541
CONVERSION_LITROS_A_GALONES = 1 / 3.78541
PRECIO_POR_LITRO = 1.5

def maquina_turing_galones_a_litros(galones):
    cinta = list(str(galones))
    estado = 'inicio'
    cabezal = 0
    while estado != 'fin':
        if estado == 'inicio':
            if cinta[cabezal] == '.':
                estado = 'decimal'
                cabezal += 1
            else:
                cabezal += 1
        elif estado == 'decimal':
            if cabezal == len(cinta):
                estado = 'convertir'
            else:
                cabezal += 1
        elif estado == 'convertir':
            valor = float(''.join(cinta))
            litros = valor * CONVERSION_GALONES_A_LITROS
            return round(litros, 2)
            estado = 'fin'
    return 0

def maquina_turing_litros_a_galones(litros):
    cinta = list(str(litros))
    estado = 'inicio'
    cabezal = 0
    while estado != 'fin':
        if estado == 'inicio':
            if cinta[cabezal] == '.':
                estado = 'decimal'
                cabezal += 1
            else:
                cabezal += 1
        elif estado == 'decimal':
            if cabezal == len(cinta):
                estado = 'convertir'
            else:
                cabezal += 1
        elif estado == 'convertir':
            valor = float(''.join(cinta))
            galones = valor * CONVERSION_LITROS_A_GALONES
            return round(galones, 2)
            estado = 'fin'
    return 0

def convertir():
    try:
        if galones_entry.get():
            galones = float(galones_entry.get())
            litros = maquina_turing_galones_a_litros(galones)
            precio = litros * PRECIO_POR_LITRO
            litros_var.set(f"{litros:.2f}")
            precio_var.set(f"${precio:.2f}")
        elif litros_entry.get():
            litros = float(litros_entry.get())
            galones = maquina_turing_litros_a_galones(litros)
            precio = litros * PRECIO_POR_LITRO
            galones_var.set(f"{galones:.2f}")
            precio_var.set(f"${precio:.2f}")
        else:
            messagebox.showwarning("Entrada inválida", "Por favor ingrese un valor en galones o litros.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido.")

ventana = tk.Tk()
ventana.title("Conversor de Galones a Litros y Precio")

galones_label = tk.Label(ventana, text="Galones:")
galones_label.grid(row=0, column=0)
galones_entry = tk.Entry(ventana)
galones_entry.grid(row=0, column=1)

litros_label = tk.Label(ventana, text="Litros:")
litros_label.grid(row=1, column=0)
litros_entry = tk.Entry(ventana)
litros_entry.grid(row=1, column=1)

galones_var = tk.StringVar()
litros_var = tk.StringVar()
precio_var = tk.StringVar()

resultado_galones_label = tk.Label(ventana, text="Galones resultantes:")
resultado_galones_label.grid(row=2, column=0)
resultado_galones = tk.Label(ventana, textvariable=galones_var)
resultado_galones.grid(row=2, column=1)

resultado_litros_label = tk.Label(ventana, text="Litros resultantes:")
resultado_litros_label.grid(row=3, column=0)
resultado_litros = tk.Label(ventana, textvariable=litros_var)
resultado_litros.grid(row=3, column=1)

resultado_precio_label = tk.Label(ventana, text="Precio total:")
resultado_precio_label.grid(row=4, column=0)
resultado_precio = tk.Label(ventana, textvariable=precio_var)
resultado_precio.grid(row=4, column=1)

convertir_button = tk.Button(ventana, text="Convertir", command=convertir)
convertir_button.grid(row=5, column=0, columnspan=2)

ventana.mainloop()
