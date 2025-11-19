# vistas/tabla.py
import tkinter as tk
from tkinter import ttk

class Tabla:
    def __init__(self, master, titulos, columnas, data):
        self.columnas = columnas

        self.tabla = ttk.Treeview(
            master,
            columns=self.columnas,
            show="headings",
            height=10
        )

        for i, col in enumerate(self.columnas):
            self.tabla.heading(col, text=titulos[i])
            self.tabla.column(col, width=120, anchor="w")

        self.refrescar(data)

        scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.tabla.pack(fill="both", expand=True)

    def refrescar(self, data):
        
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        
        for fila in data:
            self.tabla.insert("", "end", values=fila)
