from django.shortcuts import render

from .models import *
from banner.models import *

# Create your views here.

def index(request):
    itens = Item.objects.all()
    banner = Banner.objects.all()

    return render(request, 'index.html', {'itens': itens, 'banners': banner})


def ver_item(request, id):
    item = Item.objects.get(id=id)

    return render(request, 'item.html', {'item': item})


