# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20160802_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Biograf\xeda'),
        ),
    ]
