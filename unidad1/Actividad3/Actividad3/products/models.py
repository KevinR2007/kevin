from django.db import models

# Create your models here.

class Zapatos(models.Model):
    Nombre = models.CharField(max_length=100)
    Modelo = models.CharField(max_length=100)
    Talla = models.IntegerField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Fecha_Fabricacion = models.DateField(auto_now_add=False)
    def __str__(self):
        return f"{self.Nombre} - {self.Modelo} (Talla: {self.Talla})"
