from django.db import models


# Create your models here.
class Tipo_entrega(models.Model):
    tipo = models.CharField(max_length=255)
    ativo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo
        
    class Meta:
        db_table = "tipo_entrega"
        verbose_name_plural = "Tipos de entregas"