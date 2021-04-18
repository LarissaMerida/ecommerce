from django.db import models
# Create your models here.

class Banner(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    arquivo_imagem = models.ImageField(upload_to='banner', verbose_name="Imagem", null=True, blank=True)
    arquivo_video = models.FileField(upload_to='banner', max_length=254, verbose_name="Vídeo", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "banner"
        verbose_name_plural = "Banners"

