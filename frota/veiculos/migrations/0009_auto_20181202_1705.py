# Generated by Django 2.1.3 on 2018-12-02 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0008_auto_20181202_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisicao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 17, 5, 9, 344880)),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='aut',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
