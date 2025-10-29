import tkinter as tk

class Balon():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.deporte = tk.StringVar(ventanaPrincipal)
        self.marca = tk.StringVar(ventanaPrincipal)
        self.diametro = tk.StringVar(ventanaPrincipal)
        self.fecha_de_creacion = tk.StringVar(ventanaPrincipal)
        
        self.err_deporte= tk.StringVar(ventanaPrincipal)
        self.err_marca= tk.StringVar(ventanaPrincipal)  
        self.err_diametro= tk.StringVar(ventanaPrincipal)
        self.err_fecha_de_creacion= tk.StringVar(ventanaPrincipal)
       
        self.val_deporte = tk.StringVar(ventanaPrincipal)
        self.val_marca = tk.StringVar(ventanaPrincipal)      
        self.val_diametro = tk.StringVar(ventanaPrincipal)
        self.val_fecha_de_creacion = tk.StringVar(ventanaPrincipal)