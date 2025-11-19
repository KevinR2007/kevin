import tkinter as tk

class Zapatos:
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal

       
        self.modelo = tk.StringVar(ventanaPrincipal)
        self.marca = tk.StringVar(ventanaPrincipal)
        self.talla = tk.StringVar(ventanaPrincipal)
        self.fecha = tk.StringVar(ventanaPrincipal)

      
        self.err_modelo = tk.StringVar(ventanaPrincipal)
        self.err_marca = tk.StringVar(ventanaPrincipal)
        self.err_talla = tk.StringVar(ventanaPrincipal)
        self.err_fecha = tk.StringVar(ventanaPrincipal)
