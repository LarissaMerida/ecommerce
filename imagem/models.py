from django.db import models

from item.models import Item

# Create your models here.
class Imagem(models.Model):
    arquivo_imagem = models.ImageField(upload_to='imagemItem', verbose_name="Imagem")
    item_id = models.ForeignKey(Item,  on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  
    
    class Meta:
        db_table = "imagem"
        verbose_name_plural = "Imagens"