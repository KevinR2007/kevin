import tkinter as tk

class Zapatos():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.var_modelo = tk.StringVar(ventanaPrincipal)
        self.var_marca = tk.StringVar(ventanaPrincipal)
        self.var_talla = tk.StringVar(ventanaPrincipal)
        self.var_fecha = tk.StringVar(ventanaPrincipal)

        self.ventanaPrincipal = ventanaPrincipal
        self.err_modelo = tk.StringVar(ventanaPrincipal)
        self.err_marca = tk.StringVar(ventanaPrincipal)
        self.err_talla = tk.StringVar(ventanaPrincipal)
        self.err_fecha = tk.StringVar(ventanaPrincipal)
