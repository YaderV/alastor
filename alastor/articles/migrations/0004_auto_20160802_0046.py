# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Art\xedculo', 'verbose_name_plural': 'Art\xedculos'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Secci\xf3n', 'verbose_name_plural': 'Secciones'},
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='section',
            name='slug',
            field=models.SlugField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
