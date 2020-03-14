# -*- coding: utf-8 -*-

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0005_auto_20160810_0029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='edition',
            options={'ordering': ('-number',), 'verbose_name': 'Edici\xf3n', 'verbose_name_plural': 'Ediciones'},
        ),
    ]
