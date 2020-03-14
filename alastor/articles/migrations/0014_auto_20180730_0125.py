# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20170920_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagearticle',
            name='image',
            field=models.ImageField(upload_to='article', verbose_name='Imagen de galer\xeda'),
        ),
    ]
