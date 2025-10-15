

from rest_framework import viewsets
from .models import Zapatos
from .serializers import ZapatosSerializer

class ZapatosViewSet(viewsets.ModelViewSet):
    queryset = Zapatos.objects.all()
    serializer_class = ZapatosSerializer
    




# Create your views here.
