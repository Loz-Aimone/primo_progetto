from django.contrib import admin

# Register your models here.
from .models import Genere_AL, Autore_AL, Libro_AL

admin.site.register(Genere_AL)
admin.site.register(Autore_AL)
admin.site.register(Libro_AL)