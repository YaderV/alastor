# -*- coding: utf-8 -*-

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_article_translator'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='article', verbose_name='Imagen de galer\xeda')),
                ('image_caption', models.TextField(blank=True, verbose_name='Descripci\xf3n de imagen')),
            ],
            options={
                'verbose_name': 'Imagen de galer\xeda',
                'verbose_name_plural': 'Imagenes de galer\xeda',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='article', verbose_name='Imagen de texto'),
        ),
        migrations.AddField(
            model_name='imagearticle',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
    ]
