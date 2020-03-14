# -*- coding: utf-8 -*-

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_article_image_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Author', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='article',
            name='edition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editions.Edition', verbose_name='Edici\xf3n'),
        ),
        migrations.AlterField(
            model_name='article',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Section', verbose_name='Secci\xf3n'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Link de enlace'),
        ),
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Link de enlace'),
        ),
    ]
