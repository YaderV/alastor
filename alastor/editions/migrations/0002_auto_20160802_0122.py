# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='name',
            field=models.CharField(max_length=140, verbose_name='N\xfamero'),
        ),
    ]
