from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

from api.models.clase import Zapato
from project.serializers.clase_serializer import ClaseSerializer


class Clase_APIView(APIView):
    """Lista y crea Zapatos"""

    def get(self, request, format=None):
        zapatos = Zapato.objects.all()
        serializer = ClaseSerializer(zapatos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Clase_APIView_Detail(APIView):
    """Obtiene, actualiza y elimina un zapato"""

    def get_object(self, pk):
        try:
            return Zapato.objects.get(pk=pk)
        except Zapato.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        zapato = self.get_object(pk)
        serializer = ClaseSerializer(zapato)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        zapato = self.get_object(pk)
        serializer = ClaseSerializer(zapato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        zapato = self.get_object(pk)
        zapato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
