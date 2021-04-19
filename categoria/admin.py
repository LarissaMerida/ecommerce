from django.contrib import admin
from .models import *

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria

admin.site.register(Categoria, CategoriaAdmin,)
