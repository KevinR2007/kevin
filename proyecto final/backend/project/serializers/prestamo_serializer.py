from rest_framework import serializers
from api.models.herramienta import Herramienta
from api.models.prestamo import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Prestamo.
    """

    class Meta:
        model = Prestamo
        fields = (
            "id",
            "numero",
            "herramienta_codigo",
            "responsable",
            "fecha_salida",
            "fecha_esperada",
            "fecha_devolucion",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at")

    def validate(self, attrs):
        """
        Validación personalizada para el PrestamoSerializer.
        Solo valida disponibilidad al crear un préstamo.
        """
        request = self.context.get("request")

        # Si es UPDATE, no validar disponibilidad
        if request and request.method in ("PUT", "PATCH"):
            return attrs

        codigo = attrs.get("herramienta_codigo")
        herramienta = Herramienta.objects.filter(codigo=codigo).first()

        if not herramienta:
            raise serializers.ValidationError("La herramienta no existe.")

        if herramienta.estado != "disponible":
            raise serializers.ValidationError("La herramienta no está disponible.")

        return attrs

    def update(self, instance, validated_data):
        """
        Al registrar fecha_devolucion, marcar herramienta como disponible.
        """
        fecha_dev = validated_data.get("fecha_devolucion")

        if fecha_dev and instance.fecha_devolucion is None:
            herramienta = Herramienta.objects.get(
                codigo=instance.herramienta_codigo
            )
            herramienta.estado = "disponible"
            herramienta.save(update_fields=['estado', 'updated_at'])

        return super().update(instance, validated_data)
