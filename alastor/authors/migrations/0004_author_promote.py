# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_author_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='promote',
            field=models.BooleanField(default=False, help_text='Promover autor como autor destacado en index', verbose_name='Promover'),
        ),
    ]
