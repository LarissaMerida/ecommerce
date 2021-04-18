from django.contrib import admin
from .models import *
from video.models import *
from imagem.models import *


class VideoInline(admin.TabularInline):
    model=Video
    extra = 0

class ImagemInline(admin.TabularInline):
    model=Imagem
    extra = 0

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = (ImagemInline,VideoInline, )