import tkinter as tk

class Herramienta:
    def __init__(self):
        # Campos principales
        self.codigo = tk.StringVar()
        self.nombre = tk.StringVar()
        self.categoria = tk.StringVar()
        self.ubicacion = tk.StringVar()
        self.estado = tk.StringVar()
        self.created_at = tk.StringVar()
        self.updated_at = tk.StringVar()

        # Errores
        self.err_codigo = tk.StringVar()
        self.err_nombre = tk.StringVar()
        self.err_categoria = tk.StringVar()
        self.err_ubicacion = tk.StringVar()
        self.err_estado = tk.StringVar()


        self.codigo_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.ubicacion_var = tk.StringVar()
        self.estado_var = tk.StringVar()