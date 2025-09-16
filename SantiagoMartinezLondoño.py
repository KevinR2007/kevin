from tkinter import Label    
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
ventana.config(bg="white")
ventana.geometry("320x400")
ventana.title("Santiago Martinez Londoño")  
ventana.resizable(False, False)

Titulo = tk.Label(ventana, text="Balón", fg="black", bg="white", font=("Arial", 20))
Titulo.grid(row=0, column=1, columnspan=2, pady=10)

var_deporte = tk.StringVar()
var_marca = tk.StringVar()
var_diametro = tk.StringVar()
var_fecha_de_creacion = tk.StringVar()

err_deporte = tk.StringVar()
err_marca = tk.StringVar()
err_diametro = tk.StringVar()
err_fecha_de_creacion = tk.StringVar()

tk.Label(ventana, text="Deporte:", fg="black", bg="white", font=("Arial",12)).grid(row=1, column=0, sticky="e")
deporte_Entrada1 = tk.Entry(ventana, width=20, textvariable=var_deporte)
deporte_Entrada1.grid(row=1, column=1)
tk.Label(ventana, textvariable=err_deporte, fg="red", bg="white").grid(row=2, column=1)

tk.Label(ventana, text="Marca:", fg="black", bg="white", font=("Arial",12)).grid(row=3, column=0, sticky="e")
marca_Entrada2 = tk.Entry(ventana, width=20, textvariable=var_marca)
marca_Entrada2.grid(row=3, column=1)
tk.Label(ventana, textvariable=err_marca, fg="red", bg="white").grid(row=4, column=1)

tk.Label(ventana, text="Diametro:" ,fg="black", bg="white", font=("Arial",12)).grid(row=5, column=0, sticky="e")
diametro_Entrada3 = tk.Entry(ventana, width=20, textvariable=var_diametro)
diametro_Entrada3.grid(row=5, column=1)
tk.Label(ventana, textvariable=err_diametro, fg="red", bg="white").grid(row=6, column=1)

tk.Label(ventana, text="Fecha de creación:" ,fg="black", bg="white", font=("Arial",12)).grid(row=7, column=0, sticky="e")
fecha_de_creacion_Entrada4 = tk.Entry(ventana, width=20, textvariable=var_fecha_de_creacion)
fecha_de_creacion_Entrada4.grid(row=7, column=1)
tk.Label(ventana, textvariable=err_fecha_de_creacion, fg="red", bg="white").grid(row=8, column=1)


def val_deporte(*_):
    txt = var_deporte.get()
    if validar_letras(txt):
        err_deporte.set("")
        return True
    err_deporte.set("Solo letras")
    return False

def val_marca(*_):
    txt = var_marca.get()
    if validar_letras(txt):
        err_marca.set("")
        return True
    err_marca.set("Solo letras")
    return False

def val_diametro(*_):
    txt = var_diametro.get()
    if validar_numeros(txt):
        err_diametro.set("")
        return True
    err_diametro.set("Solo números")
    return False

def val_fecha(*_):
    txt = var_fecha_de_creacion.get()
    if validar_numeros(txt):
        err_fecha_de_creacion.set("")
        return True
    err_fecha_de_creacion.set("Solo números")
    return False

def guardar():
    ok = True
    if not val_deporte():
        ok = False
    if not val_marca():
        ok = False
    if not val_diametro():
        ok = False
    if not val_fecha():
        ok = False
    if var_deporte.get().strip() == "":
        err_deporte.set("El deporte es obligatorio.")
        ok = False
    if var_marca.get().strip() == "":
        err_marca.set("La marca es obligatoria.")
        ok = False
    if var_diametro.get().strip() == "":
        err_diametro.set("El diametro es obligatorio.")
        ok = False
    if var_fecha_de_creacion.get().strip() == "":
        err_fecha_de_creacion.set("La fecha es obligatoria.")
        ok = False
    if not ok:
        messagebox.showerror("Errores de validación", "Por favor llenar todos los campos.")
        return
    messagebox.showinfo("Guardado", "Datos guardados correctamente.")


tk.Button(ventana, text="Guardar", width=22, command=guardar, bg="white", fg="black", font=("Arial", 12)).grid(row=9, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

deporte_Entrada1.bind("<KeyRelease>", val_deporte)
marca_Entrada2.bind("<KeyRelease>", val_marca)
diametro_Entrada3.bind("<KeyRelease>", val_diametro)
fecha_de_creacion_Entrada4.bind("<KeyRelease>", val_fecha)

ventana.mainloop()