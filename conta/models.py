from django.db import models

# Create your models here.
class Conta(models.Model):
    cpf = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = "conta"
        verbose_name_plural = "Contas"
