from django.db import models

from conta.models import Conta
from item.models import Item
from tipo_entrega.models import Tipo_entrega
from tipo_pagamento.models import Tipo_pagamento

# Create your models here.
class Pedido(models.Model):
    conta_id = models.ForeignKey(Conta, on_delete=models.DO_NOTHING)
    item = models.ManyToManyField(Item)
    tipo_entrega_id = models.ForeignKey(Tipo_entrega, on_delete=models.DO_NOTHING)
    tipo_pagamento_id = models.ForeignKey(Tipo_pagamento, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pedido"
        verbose_name_plural = "Pedidos"
