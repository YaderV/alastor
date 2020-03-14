# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0007_remove_edition_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Borrador'),
        ),
    ]
