from django.shortcuts import render

from .models import *
from banner.models import *
from categoria.models import *
from django.db.models import Q

# Create your views here.

def index(request):
    itens = Item.objects.all()
    banner = Banner.objects.all()
    categorias = Categoria.objects.all()

    return render(request, 'index.html', {'itens': itens, 'banners': banner, 'categorias': categorias})


def ver_item(request, id):
    item = Item.objects.get(id=id)

    return render(request, 'item.html', {'item': item})

def pesquisa(request):
    pesquisa = request.POST.get('pesquisa')
    tipo = request.POST.get('tipo')
    categorias = Categoria.objects.all()

    if tipo == None:
        itens = Item.objects.filter(titulo=pesquisa)
        return render(request, "itens.html", {"categorias": categorias, "itens": itens})

    itens = Item.objects.filter(
            Q(titulo__istartswith=pesquisa)|  Q(titulo__iendswith=pesquisa) |  Q(titulo__icontains=pesquisa)|
            Q(titulo__startswith=pesquisa)|  Q(titulo__endswith=pesquisa) |
            Q(descricao__istartswith=pesquisa)|  Q(descricao__iendswith=pesquisa) |  Q(descricao__icontains=pesquisa)|
            Q(descricao__startswith=pesquisa)|  Q(descricao__endswith=pesquisa)
        )
    return render(request, "itens.html", {"categorias": categorias, "itens": itens})



