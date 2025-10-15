from rest_framework import viewsets
from .models import Balon
from .serializers import BalonSerializer    

class BalonViewSet(viewsets.ModelViewSet):
    queryset = Balon.objects.all()
    serializer_class = BalonSerializer

# Create your views here.
