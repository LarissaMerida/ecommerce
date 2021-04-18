from django.contrib import admin
from .models import *

# Register your models here.
class TipoEntregaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'ativo',)
    list_filter = ('ativo',)
    search_fields = ['tipo']

    model = Tipo_entrega

admin.site.register(Tipo_entrega, TipoEntregaAdmin,)
