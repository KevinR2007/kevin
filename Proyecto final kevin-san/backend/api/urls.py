from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api.views.prestamo_view import PrestamoViewSet
from api.views.herramienta_view import HerramientaViewSet


router = DefaultRouter()
router.register(r'herramientas', HerramientaViewSet, basename='herramienta')
router.register(r'prestamos', PrestamoViewSet, basename='prestamo')

urlpatterns = [
    path('', include(router.urls)),
]
