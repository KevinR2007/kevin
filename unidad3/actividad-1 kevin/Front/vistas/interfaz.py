import tkinter as tk
from tkinter import messagebox
from controladores.validaciones import Validaciones
from controladores.comunicacion import Comunicacion
from modelos.zapatos import Zapatos
from vistas.tabla import Tabla


class Interfaz:

    @staticmethod
    def mostrar_interfaz():
        ventana = tk.Tk()
        ventana.title("Zapatos - Kevin")
        ventana.geometry("480x650")

        comunicacion = Comunicacion()
        zapatos = Zapatos(ventana)

       
        tk.Label(ventana, text="Gestión de Zapatos", font=("Arial", 16, "bold")).pack(pady=10)

        
        tk.Label(ventana, text="ID ", font=("Arial", 11)).pack(anchor="w", padx=10)
        var_id = tk.StringVar()
        entry_id = tk.Entry(ventana, textvariable=var_id, width=25)
        entry_id.pack(padx=10)
        lbl_error_id = tk.Label(ventana, text="", fg="red")
        lbl_error_id.pack(anchor="w", padx=10)


        def crear_campo(nombre, variable):
            tk.Label(ventana, text=nombre, font=("Arial", 11)).pack(anchor="w", padx=10)
            entry = tk.Entry(ventana, textvariable=variable, width=25)
            entry.pack(padx=10)
            lbl = tk.Label(ventana, text="", fg="red")
            lbl.pack(anchor="w", padx=10)
            return entry, lbl

        entry_modelo, lbl_error_modelo = crear_campo("Modelo", zapatos.modelo)
        entry_marca, lbl_error_marca = crear_campo("Marca", zapatos.marca)
        entry_talla, lbl_error_talla = crear_campo("Talla", zapatos.talla)
        entry_fecha, lbl_error_fecha = crear_campo("Fecha de fabricacion", zapatos.fecha)



        def val_modelo(*args):
            if zapatos.modelo.get().strip() == "":
                lbl_error_modelo.config(text="Campo obligatorio")
            elif not Validaciones.validar_letras(zapatos.modelo):
                lbl_error_modelo.config(text="Solo letras")
            else:
                lbl_error_modelo.config(text="")

        def val_marca(*args):
            if zapatos.marca.get().strip() == "":
                lbl_error_marca.config(text="Campo obligatorio")
            elif not Validaciones.validar_letras(zapatos.marca):
                lbl_error_marca.config(text="Solo letras")
            else:
                lbl_error_marca.config(text="")

        def val_talla(*args):
            if zapatos.talla.get().strip() == "":
                lbl_error_talla.config(text="Campo obligatorio")
            elif not Validaciones.validar_numeros(zapatos.talla):
                lbl_error_talla.config(text="Solo números")
            else:
                lbl_error_talla.config(text="")

        def val_fecha(*args):
            if zapatos.fecha.get().strip() == "":
                lbl_error_fecha.config(text="Campo obligatorio")
            elif not Validaciones.validar_numeros(zapatos.fecha):
                lbl_error_fecha.config(text="Solo números")
            else:
                lbl_error_fecha.config(text="")

        

        def actualizar_tabla():
            registros = comunicacion.consultarTodo()
            if registros is None:  # evita iterar sobre None
                messagebox.showerror("Error", "No se pudieron obtener los zapatos. ¿Está corriendo el servidor?")
                return
            data = [(r["id"], r["modelo"], r["marca"], r["talla"], r["fecha"]) for r in registros]
            tabla.refrescar(data)



       

        def guardar():

            
            val_modelo()
            val_marca()
            val_talla()
            val_fecha()

            if (lbl_error_modelo.cget("text") or lbl_error_marca.cget("text")
                or lbl_error_talla.cget("text") or lbl_error_fecha.cget("text")):
                messagebox.showerror("Error", "Corrige los campos en rojo")
                return

            id_existente = var_id.get()

            
            if id_existente.isdigit():
                r = comunicacion.actualizar(
                    id_existente,
                    zapatos.modelo.get(),
                    zapatos.marca.get(),
                    zapatos.talla.get(),
                    zapatos.fecha.get()
                )

                if r:
                    messagebox.showinfo("Éxito", "Zapato actualizado")
                    actualizar_tabla()
                else:
                    messagebox.showerror("Error", "ID no existe")
                return

            
            comunicacion.guardar(
                zapatos.modelo.get(),
                zapatos.marca.get(),
                zapatos.talla.get(),
                zapatos.fecha.get()
            )

            messagebox.showinfo("Éxito", "Zapato guardado correctamente")
            actualizar_tabla()

            
            var_id.set("")
            zapatos.modelo.set("")
            zapatos.marca.set("")
            zapatos.talla.set("")
            zapatos.fecha.set("")


        def consultar_uno():

            if not var_id.get().isdigit():
                messagebox.showerror("Error", "ID inválido")
                return

            r = comunicacion.consultar(var_id.get())

            if "error" in r:
                messagebox.showinfo("Aviso", r["error"])
                return

            zapatos.modelo.set(r["modelo"])
            zapatos.marca.set(r["marca"])
            zapatos.talla.set(r["talla"])
            zapatos.fecha.set(r["fecha"])

            tabla.refrescar([
                (r["id"], r["modelo"], r["marca"], r["talla"], r["fecha"])
            ])

        def borrar():
            """Función para borrar un zapato por ID"""
            if not var_id.get().strip():
                messagebox.showerror("Error", "Ingrese un ID para borrar")
                return
                
            if not var_id.get().isdigit():
                messagebox.showerror("Error", "ID debe ser un número válido")
                return

            respuesta = messagebox.askyesno(
                "Confirmar borrado", 
                f"¿Está seguro de que desea borrar el zapato con ID {var_id.get()}?"
            )
            
            if respuesta:
                resultado = comunicacion.eliminar(var_id.get())
                
                if resultado:
                    messagebox.showinfo("Éxito", "Zapato borrado correctamente")
                    var_id.set("")
                    zapatos.modelo.set("")
                    zapatos.marca.set("")
                    zapatos.talla.set("")
                    zapatos.fecha.set("")
                    actualizar_tabla()
                else:
                    messagebox.showerror("Error", "No se encontró el zapato con ese ID")

        

        frame_botones = tk.Frame(ventana)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Guardar", width=12, command=guardar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Consultar 1", width=12, command=consultar_uno).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Consultar todos", width=15, command=actualizar_tabla).grid(row=0, column=2, padx=5)
        
        # Botón de borrar agregado en la misma fila
        tk.Button(frame_botones, text="Borrar", width=12, command=borrar).grid(row=0, column=3, padx=5)

       

        frame_tabla = tk.Frame(ventana)
        frame_tabla.pack(fill="both", expand=True, pady=10)

        titulos = ["ID", "Modelo", "Marca", "Talla", "Fecha"]
        columnas = ["id", "modelo", "marca", "talla", "fecha"]

        tabla = Tabla(frame_tabla, titulos, columnas, [])
        tabla.tabla.pack(fill="both", expand=True)

       
        entry_modelo.bind("<KeyRelease>", val_modelo)
        entry_marca.bind("<KeyRelease>", val_marca)
        entry_talla.bind("<KeyRelease>", val_talla)
        entry_fecha.bind("<KeyRelease>", val_fecha)

        ventana.mainloop()