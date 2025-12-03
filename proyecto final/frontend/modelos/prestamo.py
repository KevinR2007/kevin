import tkinter as tk

class Prestamo:
    def __init__(self):
        # Campos principales
        self.numero = tk.StringVar()
        self.herramienta_codigo = tk.StringVar()
        self.responsable = tk.StringVar()
        self.fecha_salida = tk.StringVar()
        self.fecha_esperada = tk.StringVar()
        self.fecha_devolucion = tk.StringVar()
        self.created_at = tk.StringVar()
        self.updated_at = tk.StringVar()

        # Errores
        self.err_numero = tk.StringVar()
        self.err_herramienta_codigo = tk.StringVar()
        self.err_responsable = tk.StringVar()
        self.err_fecha_salida = tk.StringVar()
        self.err_fecha_esperada = tk.StringVar()
        self.err_fecha_devolucion = tk.StringVar()

        self.numero_var = tk.StringVar()
        self.herr_codigo_var = tk.StringVar()
        self.responsable_var = tk.StringVar()
        self.fecha_salida_var = tk.StringVar()
        self.fecha_esperada_var = tk.StringVar()
        self.fecha_devolucion_var = tk.StringVar()