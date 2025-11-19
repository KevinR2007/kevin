from django.db import models

class Zapato(models.Model):
    modelo = models.CharField(max_length=200)
    marca  = models.CharField(max_length=100)
    talla  = models.CharField(max_length=20)
    fecha  = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.modelo} - {self.marca} (talla {self.talla})"


