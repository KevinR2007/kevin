from rest_framework import serializers
from .models import Zapatos

class ZapatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zapatos
        fields = '__all__'