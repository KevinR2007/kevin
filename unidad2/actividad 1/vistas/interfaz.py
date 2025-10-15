from tkinter import Label
import tkinter as tk
from tkinter import messagebox
from modelos.zapatos import Zapatos
from controladores.validaciones import Validaciones
#falta el evento de validaciónes y poder por / en la fecha y cm en la talla
 

class Interfaz():
    def mostrar_interfaz():
        ventana = tk.Tk()
        zapatos = Zapatos(ventana)
        ventana.title("Kevin Alejandro")
        ventana.geometry("320x320")
        ventana.configure(bg="#f0f0f0")
        ventana.resizable(False, False)


    
        def val_modelo(*_):
            txt = zapatos.var_modelo.get()
            if Validaciones.validar_letras(txt):
                zapatos.err_modelo.set("")
                return True
            zapatos.err_modelo.set("Solo letras")
            return False

        def val_marca(*_):
            txt = zapatos.var_marca.get()
            if Validaciones.validar_letras(txt):
                zapatos.err_marca.set("")
                return True
            zapatos.err_marca.set("Solo letras")
            return False

        def val_talla(*_):
            txt = zapatos.var_talla.get()
            if Validaciones.validar_numeros(txt):
                zapatos.err_talla.set("")
                return True
            zapatos.err_talla.set("Solo números")
            return False

        def val_fecha(*_):
            txt = zapatos.var_fecha.get()
            if Validaciones.validar_numeros(txt):
                zapatos.err_fecha.set("")
                return True
            zapatos.err_fecha.set("Solo números")
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
            if zapatos.var_modelo.get().strip() == "":
                zapatos.err_modelo.set("El modelo es obligatorio.")
                ok = False
            if zapatos.var_marca.get().strip() == "":
                zapatos.err_marca.set("La marca es obligatoria.")
                ok = False
            if zapatos.var_talla.get().strip() == "":
                zapatos.err_talla.set("La talla es obligatoria.")
                ok = False
            if zapatos.var_fecha.get().strip() == "":
                zapatos.err_fecha.set("La fecha es obligatoria.")
                ok = False
            if not ok:
                messagebox.showerror("Errores de validación", "Por favor llenar todos los campos.")
                return
            messagebox.showinfo("Guardado", "Datos guardados correctamente.")

        tk.Label(ventana, text="Zapatos", font=("Arial", 16, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=(12, 18))


        tk.Label(ventana, text="Modelo:", bg="#f0f0f0", anchor="w").grid(row=1, column=0, padx=12, pady=4, sticky="w")
        entry_modelo = tk.Entry(ventana, width=22, textvariable=zapatos.var_modelo)
        entry_modelo.grid(row=1, column=1, padx=12, pady=4)
        tk.Label(ventana, textvariable=zapatos.err_modelo, fg="#c1121f", bg="#f0f0f0").grid(row=2, column=1, sticky="w", padx=12)


        tk.Label(ventana, text="Marca:", bg="#f0f0f0", anchor="w").grid(row=3, column=0, padx=12, pady=4, sticky="w")
        entry_marca = tk.Entry(ventana, width=22, textvariable=zapatos.var_marca)
        entry_marca.grid(row=3, column=1, padx=12, pady=4)
        tk.Label(ventana, textvariable=zapatos.err_marca, fg="#c1121f", bg="#f0f0f0").grid(row=4, column=1, sticky="w", padx=12)


        tk.Label(ventana, text="Talla:", bg="#f0f0f0", anchor="w").grid(row=5, column=0, padx=12, pady=4, sticky="w")
        entry_talla = tk.Entry(ventana, width=22, textvariable=zapatos.var_talla)
        entry_talla.grid(row=5, column=1, padx=12, pady=4)
        tk.Label(ventana, textvariable=zapatos.err_talla, fg="#c1121f", bg="#f0f0f0").grid(row=6, column=1, sticky="w", padx=12)


        tk.Label(ventana, text="Fecha de fabricación:", bg="#f0f0f0", anchor="w").grid(row=7, column=0, padx=12, pady=4, sticky="w")
        entry_fecha = tk.Entry(ventana, width=22, textvariable=zapatos.var_fecha)
        entry_fecha.grid(row=7, column=1, padx=12, pady=4)
        tk.Label(ventana, textvariable=zapatos.err_fecha, fg="#c1121f", bg="#f0f0f0").grid(row=8, column=1, sticky="w", padx=12)


        tk.Button(ventana, text="Guardar", width=22, command=guardar, bg="#020202", fg="white", font=("Arial", 11, "bold")).grid(row=9, column=0, columnspan=2, pady=16)


        entry_modelo.bind("<KeyRelease>", val_modelo)
        entry_marca.bind("<KeyRelease>", val_marca)
        entry_talla.bind("<KeyRelease>", val_talla)
        entry_fecha.bind("<KeyRelease>", val_fecha)

        ventana.mainloop()
