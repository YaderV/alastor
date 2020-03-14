# -*- coding: utf-8 -*-

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_edicion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publication_date',
        ),
    ]
