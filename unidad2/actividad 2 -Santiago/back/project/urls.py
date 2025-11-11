from django.contrib import admin
from django.urls import path
from .views.clase_view import *
from .views.post_view import *

app_name = 'api'

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas para POST
    path('v1/post', Post_APIView.as_view()), 
    path('v1/post/<int:pk>/', Post_APIView_Detail.as_view()),

    # Rutas para CLASE
    path('v1/clase', Clase_APIView.as_view()), 
    path('v1/clase/<int:pk>/', Clase_APIView_Detail.as_view()),
]
