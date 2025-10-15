from django.db import models

class Balon(models.Model):
    deporte = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    diametro = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_fabricacion = models.DateField()

    def __str__(self):
        return f"{self.marca} - {self.deporte}"

# Create your models here.
