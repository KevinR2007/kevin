from rest_framework import serializers
from api.models.clase import Zapato

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zapato
        fields = ['id','modelo','marca','talla']
        exclude = ['fecha']


