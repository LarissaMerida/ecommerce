from django.db import models

# Create your models here.
class Conta(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    email = models.EmailField(unique = True, verbose_name="E-mail")
    senha = models.CharField(max_length=255)
    conf_senha = models.CharField(max_length=255)

    class Meta:
        db_table = "conta"
        verbose_name_plural = "Contas"
