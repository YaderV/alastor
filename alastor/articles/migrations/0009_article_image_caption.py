# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_caption',
            field=models.TextField(blank=True, verbose_name='Descripci\xf3n de imagen'),
        ),
    ]
