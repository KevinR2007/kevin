from django.db import models

class Clase(models.Model):
    deporte = models.CharField(max_length=100, null=True, blank=True)
    marca = models.CharField(max_length=100)
    diametro = models.FloatField(null=True, blank=True)  # 👈 agregamos esto
    fecha_de_creacion = models.DateField()

    def __str__(self):
        return (
            f"Deporte: {self.deporte}\n"
            f"Marca: {self.marca}\n"
            f"Diámetro: {self.diametro} cm\n"
            f"Fecha de creación: {self.fecha_de_creacion}"
        )
