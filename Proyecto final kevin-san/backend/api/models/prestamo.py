from django.db import models

class Prestamo(models.Model):
    numero = models.CharField(max_length=50, unique=True)
    herramienta_codigo = models.CharField(max_length=50)  # referencia por código, NO FK
    responsable = models.CharField(max_length=200)
    fecha_salida = models.DateTimeField()
    fecha_esperada = models.DateTimeField()
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Prestamo {self.numero} -> {self.herramienta_codigo}"
