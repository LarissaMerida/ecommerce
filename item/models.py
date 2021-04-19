from django.db import models
from categoria.models import *

# Create your models here.
class Item(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.FloatField(verbose_name="Preço")
    categoria_id = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "item"
        verbose_name_plural = "Itens"