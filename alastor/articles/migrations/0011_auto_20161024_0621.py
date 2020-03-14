# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20161018_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_translation',
            field=models.BooleanField(default=False, verbose_name='Traducci\xf3n'),
        ),
        migrations.AddField(
            model_name='article',
            name='translation_body',
            field=models.TextField(blank=True, verbose_name='Texto traducido'),
        ),
    ]
