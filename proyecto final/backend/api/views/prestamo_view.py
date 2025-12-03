from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models.prestamo import Prestamo
from api.models.herramienta import Herramienta
from project.serializers.prestamo_serializer import PrestamoSerializer
#ya agarraron los import, era que faltaba __init__.py en la ruta a importar, entonces django no reconocia la carpeta como un modulo



class PrestamoViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Prestamo.
    Create: valida existencia y disponibilidad de la herramienta (por codigo),
            actualiza estado de herramienta a 'prestada'.
    Update: si se registra fecha_devolucion (antes nula) marca herramienta como 'disponible'.
    """
    queryset = Prestamo.objects.all().order_by('numero')
    serializer_class = PrestamoSerializer
    lookup_field = "numero"

    def create(self, request, *args, **kwargs):
        data = request.data
        codigo = data.get('herramienta_codigo')

        if not codigo:
            return Response(
                {"error": "herramienta_codigo es obligatorio"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Verificar herramienta
        try:
            herramienta = Herramienta.objects.get(codigo=codigo)
        except Herramienta.DoesNotExist:
            return Response(
                {"error": "Herramienta no encontrada"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Validar disponibilidad
        if herramienta.estado.lower() != 'disponible':
            return Response(
                {"error": "Herramienta no disponible"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Serializar y guardar préstamo
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Actualizar estado de la herramienta a 'prestada'
        herramienta.estado = 'prestada'
        herramienta.save(update_fields=['estado', 'updated_at'])

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

    # Guardamos el código de la herramienta antes de borrar el préstamo
        herramienta_codigo = instance.herramienta_codigo

    # Eliminamos el préstamo
        self.perform_destroy(instance)

    # Después de borrar, liberamos la herramienta
        try:
            herramienta = Herramienta.objects.get(codigo=herramienta_codigo)
            herramienta.estado = 'disponible'
            herramienta.save(update_fields=['estado', 'updated_at'])
        except Herramienta.DoesNotExist:
            pass  # Si no existe la herramienta, simplemente ignoramos
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    






