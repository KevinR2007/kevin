from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
