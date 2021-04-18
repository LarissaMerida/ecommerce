# Generated by Django 3.2 on 2021-04-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Contas',
                'db_table': 'conta',
            },
        ),
    ]
