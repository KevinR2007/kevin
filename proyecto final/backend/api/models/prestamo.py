from django.db import models


class Prestamo(models.Model):
    """
    modelo que presenta un préstamo de herramienta dentro del sistema de inventario.
    
    atributos:
        numero (str): Número único autogenerado para identificar el préstamo.
        herramienta_codigo (str): Código de la herramienta prestada (referencia por código, no FK).
        responsable (str): Nombre de la persona responsable del préstamo.
        fecha_salida (datetime): Fecha y hora en que se realizó el préstamo.
        fecha_esperada (datetime): Fecha y hora esperada para la devolución.
        fecha_devolucion (datetime): Fecha y hora en que se devolvió la herramienta (puede ser nulo).
        created_at (datetime): Fecha de creación automática.
        updated_at (datetime): Fecha de última actualización automática.
    """
    numero = models.CharField(max_length=50, unique=True)
    herramienta_codigo = models.CharField(max_length=50)  # referencia por código, NO FK
    responsable = models.CharField(max_length=200)
    fecha_salida = models.DateTimeField()
    fecha_esperada = models.DateTimeField()
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Retorna una presentación visible del préstamo. """
        return f"Prestamo {self.numero} -> {self.herramienta_codigo}"


    def generar_numero_prestamo(self):
        """
        Genera un número automático con el formato:
        PR-001, PR-002, PR-003...

        Busca el último registro creado, extrae el número y lo incrementa.
        Si no existe ningún registro, inicia en PR-001.

        Returns:
            str: Número único generado.
        """
        ultimo = Prestamo.objects.order_by('id').last()
        if not ultimo:
            return "PR-001"

        numero = int(ultimo.numero.split("-")[1])
        return f"PR-{numero + 1:03d}"
    
    def save(self, *args, **kwargs):
        """
        sobrescribe el metoto save() para asignar automáticamente un número
        de prestamo si el usuario no lo ingresó manualmente.
        
        Garantiza que cada prestamo tenga un número único.
        """
        if not self.numero:
            self.numero = self.generar_numero_prestamo()
        super().save(*args, **kwargs)
