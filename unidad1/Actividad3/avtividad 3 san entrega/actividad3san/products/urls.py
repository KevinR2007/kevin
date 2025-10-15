from rest_framework import routers
from .views   import BalonViewSet
from django.urls import path, include
router = routers.DefaultRouter()
router.register(r'balones', BalonViewSet)

urlpatterns = [
    path ('', include(router.urls)),  
]

