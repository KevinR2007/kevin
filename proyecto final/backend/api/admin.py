from django.contrib import admin
from .models.prestamo import Prestamo
from .models.herramienta import Herramienta

"""
admin personalisado para los modelos Herramienta y Prestamo.
Este archivo maneja como se visualizan Herramienta y Prestamo en el admin de Django.
"""
admin.site.register(Herramienta)
class HerramientaAdmin(admin.ModelAdmin):
    """
    Configuracion personalizada para el modelo Herramienta en el admin de Django.
    
    list_display columnas visibles en la tanbla admin.
    
    search_fields campos por los que se puede buscar.
    
    ordering orden predeterminado de los registros.
    """
    list_display = ('codigo','nombre','categoria','ubicacion','estado','created_at')
    search_fields = ('codigo','nombre','categoria','ubicacion','estado')
    ordering = ('codigo',)

admin.site.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    """
    Configuracion personalizada para el modelo Prestamo en el admin de Django.
    
    list_display columnas visibles en la tanbla admin.
    
    search_fields campos por los que se puede buscar.
    
    ordering orden predeterminado de los registros.
    """
    list_display = ('numero','herramienta_codigo','responsable','fecha_salida','fecha_esperada','fecha_devolucion','created_at')
    search_fields = ('numero','herramienta_codigo','responsable')
    ordering = ('numero',)
