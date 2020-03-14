# -*- coding: utf-8 -*-

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_author_bio'),
        ('articles', '0011_auto_20161024_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='translator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_translator', to='authors.Author', verbose_name='Traductor'),
        ),
    ]
