from django.contrib import admin
from .models import *
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    model = Banner

admin.site.register(Banner, BannerAdmin,)
