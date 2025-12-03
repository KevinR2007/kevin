# vistas/interfaz_principal.py
"""
Ventana principal del sistema IHEP
Muestra las pestañas:
- Herramientas
- Préstamos
- Búsqueda
"""

import tkinter as tk
from tkinter import ttk

from vistas.vista_herramientas import VistaHerramientas
from vistas.vista_prestamos import VistaPrestamos
from vistas.vista_busqueda import VistaBusqueda

# -------- HILOS --------
from hilos.hilo_respaldo import HiloRespaldo
from hilos.config.config_respaldo import asegurar_archivo_config, leer_intervalo_respaldo
from hilos.respaldo_util import (
    obtener_herramientas,
    obtener_prestamos,
    armar_contenido_respaldo,
    guardar_respaldo
)


class InterfazPrincipal(tk.Tk):
    """Ventana principal con pestañas del sistema IHEP."""

    def __init__(self):
        super().__init__()
        
        self.asegurar_archivo_config = asegurar_archivo_config

        self.title("IHEP - Sistema de Inventario de Herramientas y Préstamos")
        self.geometry("900x600")

        self._crear_pestanas()

        # ----------------------------
        # CARGAR DATOS DEL BACKEND
        # ----------------------------
        try:
            self.herramientas.cargar_datos_backend()
        except:
            pass

        try:
            self.prestamos.cargar_datos_backend()
        except:
            pass
        # Asegurar que el archivo de configuración exista
        self.asegurar_archivo_config()
        
        # ----------------------------
        # INICIAR HILO DE RESPALDO
        # ----------------------------
        self._iniciar_hilo_respaldo()

    # ----------------------------------------------------------------------
    def _crear_pestanas(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        # Crear vistas principales primero
        self.herramientas = VistaHerramientas(notebook)
        self.prestamos = VistaPrestamos(notebook)

        # Vista de búsqueda recibe las vistas anteriores
        self.busqueda = VistaBusqueda(notebook, self.herramientas, self.prestamos)

        # Agregar pestañas
        notebook.add(self.herramientas, text="Herramientas")
        notebook.add(self.prestamos, text="Préstamos")
        notebook.add(self.busqueda, text="Búsqueda")

    # ----------------------------------------------------------------------
    def _iniciar_hilo_respaldo(self):

        # Función interna: junta herramientas + préstamos
        def obtener_datos():
            herramientas = obtener_herramientas()
            prestamos = obtener_prestamos()
            return armar_contenido_respaldo(herramientas, prestamos)

        # Crear hilo
        hilo = HiloRespaldo(
            obtener_intervalo=leer_intervalo_respaldo,
            obtener_datos=obtener_datos,
            guardar_respaldo=guardar_respaldo
        )

        hilo.start()
        self.hilo_respaldo = hilo  # por si necesitas manipularlo luego
