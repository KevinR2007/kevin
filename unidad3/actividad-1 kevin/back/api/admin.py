from django.contrib import admin
from .models.clase import Zapato
from .models.post import Post

@admin.register(Zapato)
class ZapatoAdmin(admin.ModelAdmin):
    list_display = ('id','modelo','marca','talla','fecha')
    search_fields = ('modelo','marca')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','created_at')
