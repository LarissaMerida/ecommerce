from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Categoria")

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "categoria"
        verbose_name_plural = "Categorias"
