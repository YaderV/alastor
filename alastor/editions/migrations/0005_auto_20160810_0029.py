# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0004_edition_publication_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edition',
            name='slug',
        ),
        migrations.AlterField(
            model_name='edition',
            name='number',
            field=models.PositiveIntegerField(unique=True, verbose_name='N\xfamero'),
        ),
    ]
