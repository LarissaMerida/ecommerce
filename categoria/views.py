from django.shortcuts import render
from .models import *
from item.models import *

# Create your views here.

def categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    itens = Item.objects.filter(categoria_id=categoria.id)
    categorias = Categoria.objects.all()

    return render(request, "categoria.html", {"categoria": categoria, 'itens': itens, 'categorias': categorias})
