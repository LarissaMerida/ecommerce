from django.db import models

from item.models import Item


# Create your models here.
class Video(models.Model):
    item_id = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    arquivo_video = models.CharField(max_length=255, verbose_name="Vídeo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "video"
        verbose_name_plural = "Vídeos"

