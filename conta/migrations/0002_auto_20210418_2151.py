# Generated by Django 3.2 on 2021-04-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True, verbose_name='E-mail'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conta',
            name='endereco',
            field=models.CharField(default=1, max_length=255, verbose_name='Endereço'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conta',
            name='nome',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
