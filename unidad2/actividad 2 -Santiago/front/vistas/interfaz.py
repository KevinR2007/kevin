import tkinter as tk
from tkinter import Label    
from tkinter import messagebox
from controladores.validaciones import Validaciones
from modelos.balon import Balon


class Interfaz():

    def mostrar_interfaz():
        ventanaPrincipal = tk.Tk()
        balon = Balon(ventanaPrincipal)
        ventanaPrincipal.config(bg="white")
        ventanaPrincipal.geometry("320x400")
        ventanaPrincipal.title("Santiago Martinez Londoño")  
        
        Titulo = tk.Label(ventanaPrincipal, text="Balón", fg="black", bg="white", font=("Arial", 20))
        Titulo.grid(row=0, column=1, columnspan=2, pady=10)
        
        
        def evento_presionar_tecla(evento):
            # deporte
            if Validaciones.validar_letras(balon.deporte):
                balon.err_deporte.set("")
            else:
                balon.err_deporte.set("Solo se permiten letras")
            # marca
            if Validaciones.validar_letras(balon.marca):
                balon.err_marca.set("")
            else:
                balon.err_marca.set("Solo se permiten letras")
            # diametro
            if Validaciones.validar_numeros(balon.diametro):
                balon.err_diametro.set("")
            else:
                balon.err_diametro.set("Solo se permiten números")
            # fecha de creación 
            if Validaciones.validar_numeros(balon.fecha_de_creacion):
                balon.err_fecha_de_creacion.set("")
            else:
                balon.err_fecha_de_creacion.set("Solo se permiten números")
        
        tk.Label(ventanaPrincipal, text="Deporte:", fg="black", bg="white", font=("Arial",12)).grid(row=1, column=0, sticky="e")
        entry_deporte = tk.Entry(ventanaPrincipal, width=20, textvariable=balon.deporte)
        entry_deporte.grid(row=1, column=1)
        tk.Label(ventanaPrincipal, textvariable=balon.err_deporte, fg="red", bg="white").grid(row=2, column=1)

        tk.Label(ventanaPrincipal, text="Marca:", fg="black", bg="white", font=("Arial",12)).grid(row=3, column=0, sticky="e")
        entry_marca = tk.Entry(ventanaPrincipal, width=20, textvariable=balon.marca)
        entry_marca.grid(row=3, column=1)
        tk.Label(ventanaPrincipal, textvariable=balon.err_marca, fg="red", bg="white").grid(row=4, column=1)
        
        
        tk.Label(ventanaPrincipal, text="Diametro:" ,fg="black", bg="white", font=("Arial",12)).grid(row=5, column=0, sticky="e")
        entry_diametro = tk.Entry(ventanaPrincipal, width=20, textvariable=balon.diametro)
        entry_diametro.grid(row=5, column=1)
        tk.Label(ventanaPrincipal, textvariable=balon.err_diametro, fg="red", bg="white").grid(row=6, column=1)
        
        
        tk.Label(ventanaPrincipal, text="Fecha de creación:" ,fg="black", bg="white", font=("Arial",12)).grid(row=7, column=0, sticky="e")
        entry_fecha_de_creacion = tk.Entry(ventanaPrincipal, width=20, textvariable=balon.fecha_de_creacion)
        entry_fecha_de_creacion.grid(row=7, column=1)
        tk.Label(ventanaPrincipal, textvariable=balon.err_fecha_de_creacion, fg="red", bg="white").grid(row=8, column=1)
        
        
    
        def val_deporte(*_):
            txt = balon.deporte.get()
            if Validaciones.validar_letras(balon.deporte):
                balon.err_deporte.set("")
                return True
            balon.err_deporte.set("Solo letras")
            return False

        def val_marca(*_):
            txt = balon.marca.get()
            if Validaciones.validar_letras(balon.marca):
                balon.err_marca.set("")
                return True
            balon.err_marca.set("Solo letras")
            return False

        def val_diametro(*_):
            txt = balon.diametro.get()
            if Validaciones.validar_numeros(balon.diametro):
                balon.err_diametro.set("")
                return True
            balon.err_diametro.set("Solo números")
            return False

        def val_fecha(*_):
            txt = balon.fecha_de_creacion.get()
            if Validaciones.validar_numeros(balon.fecha_de_creacion):
                balon.err_fecha_de_creacion.set("")
                return True
            balon.err_fecha_de_creacion.set("Solo números")
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
            if balon.deporte.get().strip() == "":
                balon.err_deporte.set("El deporte es obligatorio.")
                ok = False
            if balon.marca.get().strip() == "":
                balon.err_marca.set("La marca es obligatoria.")
                ok = False
            if balon.diametro.get().strip() == "":
                balon.err_diametro.set("El diametro es obligatorio.")
                ok = False
            if balon.fecha_de_creacion.get().strip() == "":
                balon.err_fecha_de_creacion.set("La fecha es obligatoria.")
                ok = False
            if not ok:
                messagebox.showerror("Errores de validación", "Por favor llenar todos los campos.")
                return
            messagebox.showinfo("Guardado", "Datos guardados correctamente.")


        
        tk.Button(ventanaPrincipal, text="Guardar", width=22, command=guardar, bg="white", fg="black", font=("Arial", 12)).grid(row=9, column=0, columnspan=2, pady=10, ipadx=10, ipady=5)

        entry_deporte.bind("<KeyRelease>", evento_presionar_tecla)
        entry_marca.bind("<KeyRelease>", evento_presionar_tecla)
        entry_diametro.bind("<KeyRelease>", evento_presionar_tecla)
        entry_fecha_de_creacion.bind("<KeyRelease>", evento_presionar_tecla)

        ventanaPrincipal.mainloop()
