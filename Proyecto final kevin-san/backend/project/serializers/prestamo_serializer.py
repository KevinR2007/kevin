from rest_framework import serializers
from api.models.prestamo import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
