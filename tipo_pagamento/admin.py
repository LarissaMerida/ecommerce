from django.contrib import admin
from .models import *

# Register your models here.
class TipoPagamentoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'ativo',)
    list_filter = ('ativo',)
    search_fields = ['tipo']
    model = Tipo_pagamento

admin.site.register(Tipo_pagamento, TipoPagamentoAdmin,)