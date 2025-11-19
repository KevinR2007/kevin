from rest_framework import serializers
from api.models.clase import Clase

class ClaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clase
        # si necsito que el usuario ingrese fecha 
        #cambiar el exclude por fields = '__all__'     
        exclude = ['fecha_de_creacion']
