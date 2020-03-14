# -*- coding: utf-8 -*-

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_author_promote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-promote', 'name'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
    ]
