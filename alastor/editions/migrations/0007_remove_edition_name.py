# -*- coding: utf-8 -*-

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0006_auto_20160810_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edition',
            name='name',
        ),
    ]
