
import tkinter as tk
from tkinter import messagebox
import re


RE_LETRAS = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]+$")

RE_NUMEROS = re.compile(r"^\d+$")

def validar_letras(texto):
    return texto == "" or RE_LETRAS.match(texto)

def validar_numeros(texto):
    return texto == "" or RE_NUMEROS.match(texto)

ventana = tk.Tk()
ventana.title("Kevin Alejandro")
ventana.geometry("320x320")
ventana.configure(bg="#f0f0f0")
ventana.resizable(False, False)


var_modelo = tk.StringVar()
var_marca = tk.StringVar()
var_talla = tk.StringVar()
var_fecha = tk.StringVar()


err_modelo = tk.StringVar()
err_marca = tk.StringVar()
err_talla = tk.StringVar()
err_fecha = tk.StringVar()

def val_modelo(*_):
    txt = var_modelo.get()
    if validar_letras(txt):
        err_modelo.set("")
        return True
    err_modelo.set("Solo letras")
    return False

def val_marca(*_):
    txt = var_marca.get()
    if validar_letras(txt):
        err_marca.set("")
        return True
    err_marca.set("Solo letras")
    return False

def val_talla(*_):
    txt = var_talla.get()
    if validar_numeros(txt):
        err_talla.set("")
        return True
    err_talla.set("Solo números")
    return False

def val_fecha(*_):
    txt = var_fecha.get()
    if validar_numeros(txt):
        err_fecha.set("")
        return True
    err_fecha.set("Solo números")
    return False

def guardar():
    ok = True
    if not val_modelo():
        ok = False
    if not val_marca():
        ok = False
    if not val_talla():
        ok = False
    if not val_fecha():
        ok = False
    if var_modelo.get().strip() == "":
        err_modelo.set("El modelo es obligatorio.")
        ok = False
    if var_marca.get().strip() == "":
        err_marca.set("La marca es obligatoria.")
        ok = False
    if var_talla.get().strip() == "":
        err_talla.set("La talla es obligatoria.")
        ok = False
    if var_fecha.get().strip() == "":
        err_fecha.set("La fecha es obligatoria.")
        ok = False
    if not ok:
        messagebox.showerror("Errores de validación", "Por favor llenar todos los campos.")
        return
    messagebox.showinfo("Guardado", "Datos guardados correctamente.")

tk.Label(ventana, text="Zapatos", font=("Arial", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=(12, 18))


tk.Label(ventana, text="Modelo:", bg="#f0f0f0", anchor="w").grid(row=1, column=0, padx=12, pady=4, sticky="w")
entry_modelo = tk.Entry(ventana, width=22, textvariable=var_modelo)
entry_modelo.grid(row=1, column=1, padx=12, pady=4)
tk.Label(ventana, textvariable=err_modelo, fg="#c1121f", bg="#f0f0f0").grid(row=2, column=1, sticky="w", padx=12)


tk.Label(ventana, text="Marca:", bg="#f0f0f0", anchor="w").grid(row=3, column=0, padx=12, pady=4, sticky="w")
entry_marca = tk.Entry(ventana, width=22, textvariable=var_marca)
entry_marca.grid(row=3, column=1, padx=12, pady=4)
tk.Label(ventana, textvariable=err_marca, fg="#c1121f", bg="#f0f0f0").grid(row=4, column=1, sticky="w", padx=12)


tk.Label(ventana, text="Talla:", bg="#f0f0f0", anchor="w").grid(row=5, column=0, padx=12, pady=4, sticky="w")
entry_talla = tk.Entry(ventana, width=22, textvariable=var_talla)
entry_talla.grid(row=5, column=1, padx=12, pady=4)
tk.Label(ventana, textvariable=err_talla, fg="#c1121f", bg="#f0f0f0").grid(row=6, column=1, sticky="w", padx=12)


tk.Label(ventana, text="Fecha de fabricación:", bg="#f0f0f0", anchor="w").grid(row=7, column=0, padx=12, pady=4, sticky="w")
entry_fecha = tk.Entry(ventana, width=22, textvariable=var_fecha)
entry_fecha.grid(row=7, column=1, padx=12, pady=4)
tk.Label(ventana, textvariable=err_fecha, fg="#c1121f", bg="#f0f0f0").grid(row=8, column=1, sticky="w", padx=12)


tk.Button(ventana, text="Guardar", width=22, command=guardar, bg="#020202", fg="white", font=("Arial", 11, "bold")).grid(row=9, column=0, columnspan=2, pady=16)


entry_modelo.bind("<KeyRelease>", val_modelo)
entry_marca.bind("<KeyRelease>", val_marca)
entry_talla.bind("<KeyRelease>", val_talla)
entry_fecha.bind("<KeyRelease>", val_fecha)

ventana.mainloop()







