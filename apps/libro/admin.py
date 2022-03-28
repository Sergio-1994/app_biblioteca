from django.contrib import admin
from .models import *

class AutorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'apellidos',
        'nacionalidad',
        'descripcion',
        'estado'
    ]

class LibroAdmin(admin.ModelAdmin):
    list_display= [
        'id',
        'titulo',
        'fecha_publicacion',
        'autor',
        'estado'
    ]

# Register your models here.
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
