# vistas/vista_busqueda.py

from tkinter import Frame, Label, Entry, Button, StringVar
from vistas.tabla import Tabla


class VistaBusqueda(Frame):

    def __init__(self, parent, vista_herramientas, vista_prestamos):
        super().__init__(parent)

        # referencias a las otras vistas
        self.vista_herramientas = vista_herramientas
        self.vista_prestamos = vista_prestamos

        Label(self, text="Búsqueda", font=("Arial", 14)).pack(pady=10)

        filtro_frame = Frame(self)
        filtro_frame.pack(pady=6)

        Label(filtro_frame, text="Buscar (código, nombre, categoría o responsable)").grid(row=0, column=0, padx=5)
        self.entrada_var = StringVar()
        Entry(filtro_frame, textvariable=self.entrada_var, width=40).grid(row=0, column=1, padx=6)

        Button(filtro_frame, text="Buscar", command=self.buscar).grid(row=0, column=2, padx=6)
        Button(filtro_frame, text="Mostrar todo", command=self.mostrar_todo).grid(row=0, column=3, padx=6)

        columnas = ["Origen", "Código", "Nombre/Responsable", "Detalle"]
        self.tabla = Tabla(self, columnas)

        self.mostrar_todo()

    # --------------------------
    # Obtener datos reales
    # --------------------------
    def obtener_herramientas(self):
        # lista_herramientas es una lista de dicts
        return self.vista_herramientas.lista_herramientas

    def obtener_prestamos(self):
        # Pedimos a VistaPrestamos una lista adecuada
        return self.vista_prestamos.obtener_filas()

    # --------------------------
    # Mostrar todo
    # --------------------------
    def mostrar_todo(self):
        data = []

        # herramientas
        for h in self.obtener_herramientas():
            data.append(("Herramienta", h["codigo"], h["nombre"], h["estado"]))

        # préstamos
        for p in self.obtener_prestamos():
            data.append(("Préstamo", p[0], p[2], p[1]))  
            # p[0]=num, p[1]=codigo, p[2]=responsable

        self.tabla.cargar_datos(data)

    # --------------------------
    # Buscar
    # --------------------------
    def buscar(self):
        termino = self.entrada_var.get().strip().lower()
        if not termino:
            self.mostrar_todo()
            return

        resultados = []

        # herramientas
        for h in self.obtener_herramientas():
            if (termino in h["codigo"].lower() or
                termino in h["nombre"].lower() or
                termino in h["categoria"].lower()):
                resultados.append(("Herramienta", h["codigo"], h["nombre"], h["estado"]))

        # préstamos
        for p in self.obtener_prestamos():
            if (termino in p[0].lower() or   # numero
                termino in p[1].lower() or   # codigo herramienta
                termino in p[2].lower()):    # responsable
                resultados.append(("Préstamo", p[0], p[2], p[1]))

        self.tabla.cargar_datos(resultados)
