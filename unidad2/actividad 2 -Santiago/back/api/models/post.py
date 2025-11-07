from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

class Post(TimeStampedModel, SoftDeletableModel):
    deporte = models.CharField(max_length=50, null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, blank=False)
    diametro = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")

    def __str__(self):
        return f"{self.marca} - {self.deporte} - {self.diametro} cm - Creado el {self.fecha_de_creacion}"
