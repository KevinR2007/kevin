from django.db import models

class Herramienta(models.Model):
    """
    Modelo que representa una herramienta dentro del sistema de inventario.

    Atributos:
        codigo (str): Código único autogenerado para identificar la herramienta.
        nombre (str): Nombre de la herramienta.
        categoria (str): Categoría o tipo de herramienta.
        ubicacion (str): Lugar físico donde se encuentra.
        estado (str): Estado actual ('disponible', 'prestada', 'dañada').
        created_at (datetime): Fecha de creación automática.
        updated_at (datetime): Fecha de última actualización automática.
    """

    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=100)  # disponible, prestada, dañada
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática
    updated_at = models.DateTimeField(auto_now=True)      # Fecha de actualización automática

    def __str__(self):
        """Retorna una representación legible de la herramienta."""
        return f"{self.codigo} - {self.nombre}"

    
    def generar_codigo_herramienta(self):
        ultimo = Herramienta.objects.order_by("-id").first()

        # Si no hay herramientas creadas aún
        if not ultimo or not ultimo.codigo:
            return "001"

        codigo_anterior = ultimo.codigo

        # Si el código tenía guion (por si acaso en el futuro)
        if "-" in codigo_anterior:
            numero_str = codigo_anterior.split("-")[1]
        else:
            numero_str = codigo_anterior  # Usa directamente el número

        try:
            numero = int(numero_str)
        except ValueError:
            numero = 0  # Evita que explote si algo está raro

        return str(numero + 1).zfill(3)

    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save() para asignar automáticamente un código
        si el usuario no lo ingresó manualmente.

        - Si 'codigo' está vacío → genera uno nuevo.
        - Si ya tiene código → solo guarda normalmente.
        """
        if not self.codigo:
            self.codigo = self.generar_codigo_herramienta()

        super().save(*args, **kwargs)
