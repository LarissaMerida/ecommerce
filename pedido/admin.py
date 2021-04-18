from django.contrib import admin
from tipo_entrega.models import *
from tipo_pagamento.models import *
from item.models import *
from .models import *

# class TipoEntregaInline(admin.TabularInline):
#     model=Tipo_entrega
#     extra = 0

# class TipoPagamentoInline(admin.TabularInline):
#     model=Tipo_pagamento
#     extra = 0

# @admin.register(Pedido)
# class PedidoAdmin(admin.ModelAdmin):
#     inlines = (TipoPagamentoInline,TipoEntregaInline, )


