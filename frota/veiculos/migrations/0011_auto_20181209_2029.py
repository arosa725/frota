# Generated by Django 2.1.3 on 2018-12-09 22:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0010_auto_20181205_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='centrocusto',
            field=models.CharField(blank=True, max_length=10, verbose_name='Centro de Custo'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='nome',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nome do Departamento'),
        ),
        migrations.AlterField(
            model_name='requisicao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 20, 29, 40, 479330)),
        ),
    ]
