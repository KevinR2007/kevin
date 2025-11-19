import tkinter as tk
from tkinter import Label
from tkinter import messagebox
from tkinter import ttk

# Importaciones correctas según tu estructura
from controladores.validaciones import Validaciones
from modelos.balon import Balon


class ControlBalon:
    def __init__(self):
        self.data = []

    def guardar(self, deporte, marca, diametro, fecha):
        nuevo = {
            "id": len(self.data) + 1,
            "deporte": deporte,
            "marca": marca,
            "diametro": diametro,
            "fecha": fecha
        }
        self.data.append(nuevo)
        return nuevo["id"]

    def editar(self, id, deporte, marca, diametro, fecha):
        try:
            id = int(id)
        except:
            return False

        for elem in self.data:
            if elem["id"] == id:
                elem["deporte"] = deporte
                elem["marca"] = marca
                elem["diametro"] = diametro
                elem["fecha"] = fecha
                return True
        return False

    def consultar(self, id):
        try:
            id = int(id)
        except:
            return {}

        for elem in self.data:
            if elem["id"] == id:
                return elem
        return {}

    def consultar_todo(self):
        return self.data

    def eliminar(self, id):
        try:
            id = int(id)
        except:
            return
        self.data = [x for x in self.data if x["id"] != id]


class Interfaz:

    def __init__(self):
        self.ventanaPrincipal = tk.Tk()
        self.ventanaPrincipal.config(bg="white")
        self.ventanaPrincipal.geometry("360x720")
        self.ventanaPrincipal.title("Santiago Martinez Londoño")

        self.control = ControlBalon()
        self.balon = Balon(self.ventanaPrincipal)

        columnas = ["id", "deporte", "marca", "diametro", "fecha"]
        titulos = ["Identificador", "Deporte", "Marca", "Diámetro", "Fecha"]

        self.tabla = ttk.Treeview(self.ventanaPrincipal, columns=columnas, show="headings", height=9)
        for t, c in zip(titulos, columnas):
            self.tabla.heading(c, text=t)
            self.tabla.column(c, width=110, anchor="center")

    def limpiar_formulario(self):
        self.balon.id.set("")
        self.balon.deporte.set("")
        self.balon.marca.set("")
        self.balon.diametro.set("")
        self.balon.fecha_de_creacion.set("")

    # --------------------------
    # CREAR NUEVO
    # --------------------------
    def accion_guardar_boton(self):
        deporte = self.balon.deporte.get()
        marca = self.balon.marca.get()
        diametro = self.balon.diametro.get()
        fecha = self.balon.fecha_de_creacion.get()

        nuevo_id = self.control.guardar(deporte, marca, diametro, fecha)
        self.balon.id.set(str(nuevo_id))
        self.refrescar_tabla()

    # --------------------------
    # CONSULTAR 1
    # --------------------------
    def accion_consultar_boton(self, id):
        if not id.strip():
            messagebox.showerror("Error", "Ingrese un ID para consultar.")
            return

        resultado = self.control.consultar(id)
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        if resultado:
            self.tabla.insert(
                "", "end",
                values=(resultado["id"], resultado["deporte"], resultado["marca"],
                        resultado["diametro"], resultado["fecha"])
            )
        else:
            messagebox.showerror("Consultar", "No encontrado.")

    # --------------------------
    # CONSULTAR TODOS
    # --------------------------
    def accion_consultar_todo(self):
        self.refrescar_tabla()

    # --------------------------
    # REFRESCAR TABLA
    # --------------------------
    def refrescar_tabla(self):
        for i in self.tabla.get_children():
            self.tabla.delete(i)

        for elem in self.control.consultar_todo():
            self.tabla.insert(
                "", "end",
                values=(elem["id"], elem["deporte"], elem["marca"], elem["diametro"], elem["fecha"])
            )

    # --------------------------
    # INTERFAZ
    # --------------------------
    def mostrar_interfaz(self):

        Titulo = tk.Label(self.ventanaPrincipal, text="Balón", fg="black", bg="white", font=("Arial", 20))
        Titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # -------------------------------------------
        # VALIDACIONES EN TIEMPO REAL (FUNCIONAN)
        # -------------------------------------------
        def evento_tecla(_):
            # deporte
            if Validaciones.validar_letras(self.balon.deporte):
                self.balon.err_deporte.set("")
            else:
                self.balon.err_deporte.set("Solo letras")

            # marca
            if Validaciones.validar_letras(self.balon.marca):
                self.balon.err_marca.set("")
            else:
                self.balon.err_marca.set("Solo letras")

            # diametro
            if Validaciones.validar_numeros(self.balon.diametro):
                self.balon.err_diametro.set("")
            else:
                self.balon.err_diametro.set("Solo números")

            # fecha
            if Validaciones.validar_numeros(self.balon.fecha_de_creacion):
                self.balon.err_fecha_de_creacion.set("")
            else:
                self.balon.err_fecha_de_creacion.set("Solo números")

        # ---------- CAMPOS ----------

        tk.Label(self.ventanaPrincipal, text="ID:", bg="white").grid(row=1, column=0, sticky="e", padx=20)
        entry_id = tk.Entry(self.ventanaPrincipal, width=25, textvariable=self.balon.id)
        entry_id.grid(row=1, column=1)

        tk.Label(self.ventanaPrincipal, textvariable=self.balon.err_id, fg="red", bg="white").grid(
            row=2, column=1)

        tk.Label(self.ventanaPrincipal, text="Deporte:", bg="white").grid(row=3, column=0, sticky="e", padx=20)
        entry_deporte = tk.Entry(self.ventanaPrincipal, width=25, textvariable=self.balon.deporte)
        entry_deporte.grid(row=3, column=1)

        tk.Label(self.ventanaPrincipal, textvariable=self.balon.err_deporte, fg="red", bg="white").grid(
            row=4, column=1)

        tk.Label(self.ventanaPrincipal, text="Marca:", bg="white").grid(row=5, column=0, sticky="e", padx=20)
        entry_marca = tk.Entry(self.ventanaPrincipal, width=25, textvariable=self.balon.marca)
        entry_marca.grid(row=5, column=1)

        tk.Label(self.ventanaPrincipal, textvariable=self.balon.err_marca, fg="red", bg="white").grid(
            row=6, column=1)

        tk.Label(self.ventanaPrincipal, text="Diámetro:", bg="white").grid(row=7, column=0, sticky="e", padx=20)
        entry_diametro = tk.Entry(self.ventanaPrincipal, width=25, textvariable=self.balon.diametro)
        entry_diametro.grid(row=7, column=1)

        tk.Label(self.ventanaPrincipal, textvariable=self.balon.err_diametro, fg="red", bg="white").grid(
            row=8, column=1)

        tk.Label(self.ventanaPrincipal, text="Fecha creación:", bg="white").grid(row=9, column=0, sticky="e", padx=20)
        entry_fecha = tk.Entry(self.ventanaPrincipal, width=25, textvariable=self.balon.fecha_de_creacion)
        entry_fecha.grid(row=9, column=1)

        tk.Label(self.ventanaPrincipal, textvariable=self.balon.err_fecha_de_creacion, fg="red", bg="white").grid(
            row=10, column=1)

        # ------------------------------------
        # BOTÓN GUARDAR (EDITA O CREA)
        # ------------------------------------
        def guardar():
            ok = True

            if not self.balon.deporte.get().strip():
                self.balon.err_deporte.set("Obligatorio")
                ok = False

            if not self.balon.marca.get().strip():
                self.balon.err_marca.set("Obligatorio")
                ok = False

            if not self.balon.diametro.get().strip():
                self.balon.err_diametro.set("Obligatorio")
                ok = False

            if not self.balon.fecha_de_creacion.get().strip():
                self.balon.err_fecha_de_creacion.set("Obligatorio")
                ok = False

            if not ok:
                messagebox.showerror("Errores", "Complete todo")
                return

            # Editar si hay ID, crear si no hay
            if self.balon.id.get().strip():
                exito = self.control.editar(
                    self.balon.id.get(),
                    self.balon.deporte.get(),
                    self.balon.marca.get(),
                    self.balon.diametro.get(),
                    self.balon.fecha_de_creacion.get()
                )
                if exito:
                    messagebox.showinfo("Editar", "Datos editados correctamente.")
                else:
                    messagebox.showerror("Error", "No existe ese ID para editar.")
            else:
                self.accion_guardar_boton()
                messagebox.showinfo("Guardado", "Datos guardados correctamente.")

            self.refrescar_tabla()

        tk.Button(self.ventanaPrincipal, text="Guardar", width=25, command=guardar).grid(
            row=11, column=0, columnspan=2, pady=10)

        tk.Button(self.ventanaPrincipal, text="Consultar 1", width=25,
                  command=lambda: self.accion_consultar_boton(self.balon.id.get())
                  ).grid(row=12, column=0, columnspan=2, pady=5)

        tk.Button(self.ventanaPrincipal, text="Consultar todos", width=25,
                  command=self.accion_consultar_todo).grid(row=13, column=0, columnspan=2, pady=5)

        # borrar
        def borrar_elemento():
            seleccion = self.tabla.selection()
            if not seleccion:
                messagebox.showerror("Error", "Seleccione un elemento para borrar.")
                return

            for i in seleccion:
                id_borrar = self.tabla.item(i)["values"][0]
                self.control.eliminar(id_borrar)
                self.tabla.delete(i)

            self.limpiar_formulario()
            self.refrescar_tabla()
            messagebox.showinfo("Borrado", "Registro eliminado correctamente.")

        tk.Button(self.ventanaPrincipal, text="Borrar", width=25, command=borrar_elemento).grid(
            row=14, column=0, columnspan=2, pady=5)

        # tabla
        self.tabla.grid(row=15, column=0, columnspan=2, pady=20)

        # seleccionar fila
        def seleccionar(_):
            for i in self.tabla.selection():
                valores = self.tabla.item(i)["values"]
                self.balon.id.set(str(valores[0]))
                self.balon.deporte.set(valores[1])
                self.balon.marca.set(valores[2])
                self.balon.diametro.set(valores[3])
                self.balon.fecha_de_creacion.set(valores[4])

        self.tabla.bind("<<TreeviewSelect>>", seleccionar)

        # validaciones
        entry_deporte.bind("<KeyRelease>", evento_tecla)
        entry_marca.bind("<KeyRelease>", evento_tecla)
        entry_diametro.bind("<KeyRelease>", evento_tecla)
        entry_fecha.bind("<KeyRelease>", evento_tecla)

        self.refrescar_tabla()

        self.ventanaPrincipal.mainloop()
