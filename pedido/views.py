from django.shortcuts import render

from .models import *
from categoria.models import *
from tipo_entrega.models import *
from tipo_pagamento.models import *

# Create your views here.

def compra(request, id):
    categorias = Categoria.objects.all()
    entregas = Tipo_entrega.objects.all()
    pagamentos = Tipo_pagamento.objects.all()

    if request.method == 'POST':
        pass
    
    return render(request, "compra.html", {"categorias": categorias, "entregas": entregas, "pagamentos": pagamentos})
