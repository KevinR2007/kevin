import tkinter as tk
from tkinter import messagebox
from controladores.validaciones import Validaciones
from modelos.zapatos import Zapatos

class Interfaz:

    def mostrar_interfaz():
        ventana = tk.Tk()
        zapatos = Zapatos(ventana)
        ventana.config(bg="white")
        ventana.geometry("340x420")
        ventana.title("Kevin - Zapatos")
        ventana.resizable(False, False)
        

        titulo = tk.Label(ventana, text="Zapatos", fg="black", bg="white", font=("Arial", 20))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

       
        def evento_presionar_tecla(evento):
            
            if Validaciones.validar_letras(zapatos.modelo):
                zapatos.err_modelo.set("")
            else:
                zapatos.err_modelo.set("Solo se permiten letras")

            if Validaciones.validar_letras(zapatos.marca):
                zapatos.err_marca.set("")
            else:
                zapatos.err_marca.set("Solo se permiten letras")

            
            if Validaciones.validar_numeros(zapatos.talla):
                zapatos.err_talla.set("")
            else:
                zapatos.err_talla.set("Solo se permiten números ")

            
            if Validaciones.validar_numeros(zapatos.fecha):
                zapatos.err_fecha.set("")
            else:
                zapatos.err_fecha.set("Solo se permiten números ")

      
        tk.Label(ventana, text="Modelo:", fg="black", bg="white", font=("Arial", 12)).grid(row=1, column=0, sticky="e")
        entry_modelo = tk.Entry(ventana, width=20, textvariable=zapatos.modelo)
        entry_modelo.grid(row=1, column=1)
        tk.Label(ventana, textvariable=zapatos.err_modelo, fg="red", bg="white").grid(row=2, column=1)

        tk.Label(ventana, text="Marca:", fg="black", bg="white", font=("Arial", 12)).grid(row=3, column=0, sticky="e")
        entry_marca = tk.Entry(ventana, width=20, textvariable=zapatos.marca)
        entry_marca.grid(row=3, column=1)
        tk.Label(ventana, textvariable=zapatos.err_marca, fg="red", bg="white").grid(row=4, column=1)

        tk.Label(ventana, text="Talla:", fg="black", bg="white", font=("Arial", 12)).grid(row=5, column=0, sticky="e")
        entry_talla = tk.Entry(ventana, width=20, textvariable=zapatos.talla)
        entry_talla.grid(row=5, column=1)
        tk.Label(ventana, textvariable=zapatos.err_talla, fg="red", bg="white").grid(row=6, column=1)

        tk.Label(ventana, text="Fecha de compra:", fg="black", bg="white", font=("Arial", 12)).grid(row=7, column=0, sticky="e")
        entry_fecha = tk.Entry(ventana, width=20, textvariable=zapatos.fecha)
        entry_fecha.grid(row=7, column=1)
        tk.Label(ventana, textvariable=zapatos.err_fecha, fg="red", bg="white").grid(row=8, column=1)

        
        def val_modelo(*_):
            if Validaciones.validar_letras(zapatos.modelo):
                zapatos.err_modelo.set("")
                return True
            zapatos.err_modelo.set("Solo letras")
            return False

        def val_marca(*_):
            if Validaciones.validar_letras(zapatos.marca):
                zapatos.err_marca.set("")
                return True
            zapatos.err_marca.set("Solo letras")
            return False

        def val_talla(*_):
            if Validaciones.validar_numeros(zapatos.talla):
                zapatos.err_talla.set("")
                return True
            zapatos.err_talla.set("Solo números ")
            return False

        def val_fecha(*_):
            if Validaciones.validar_numeros(zapatos.fecha):
                zapatos.err_fecha.set("")
                return True
            zapatos.err_fecha.set("Solo números ")
            return False

       
        def guardar():
            ok = True
            if not val_modelo(): ok = False
            if not val_marca(): ok = False
            if not val_talla(): ok = False
            if not val_fecha(): ok = False

            if zapatos.modelo.get().strip() == "":
                zapatos.err_modelo.set("El modelo es obligatorio.")
                ok = False
            if zapatos.marca.get().strip() == "":
                zapatos.err_marca.set("La marca es obligatoria.")
                ok = False
            if zapatos.talla.get().strip() == "":
                zapatos.err_talla.set("La talla es obligatoria.")
                ok = False
            if zapatos.fecha.get().strip() == "":
                zapatos.err_fecha.set("La fecha es obligatoria.")
                ok = False

            if not ok:
                messagebox.showerror("Errores de validación", "Por favor llenar todos los campos.")
                return
            messagebox.showinfo("Guardado", "Datos guardados correctamente.")

        tk.Button(
            ventana, text="Guardar", width=22, command=guardar,
            bg="white", fg="black", font=("Arial", 12)
        ).grid(row=9, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

       
        entry_modelo.bind("<KeyRelease>", evento_presionar_tecla)
        entry_marca.bind("<KeyRelease>", evento_presionar_tecla)
        entry_talla.bind("<KeyRelease>", evento_presionar_tecla)
        entry_fecha.bind("<KeyRelease>", evento_presionar_tecla)

        ventana.mainloop()
