# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0003_auto_20160808_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='publication_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de edici\xf3n'),
        ),
    ]
