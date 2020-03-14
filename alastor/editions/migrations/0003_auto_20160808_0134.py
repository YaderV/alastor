# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0002_auto_20160802_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='number',
            field=models.PositiveIntegerField(default=1, verbose_name='N\xfamero'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='edition',
            name='name',
            field=models.CharField(max_length=140, verbose_name='Nombre'),
        ),
    ]
