from rest_framework import serializers
from api.models.herramienta import Herramienta


class HerramientaSerializer(serializers.ModelSerializer):
    """
        Serializer para el modelo Herramienta.

        Permite convertir instancias de Herramienta a formatos JSON y viceversa.
    
        Atributos:
            model (Herramienta): Modelo asociado al serializer.
            fields (str): Campos del modelo a incluir en la serialización.
            read_only_fields (tuple): Campos que son de solo lectura.
    """
    class Meta:
        """
        Metadatos para el HerramientaSerializer.
        Atributos:
            model (Herramienta): Modelo asociado al serializer.
            fields (str): Campos del modelo a incluir en la serialización.
            read_only_fields (tuple): Campos que son de solo lectura.
        """
        model = Herramienta
        fields = '__all__'
        read_only_fields = ('codigo', 'created_at', 'updated_at')
