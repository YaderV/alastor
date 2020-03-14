# -*- coding: utf-8 -*-

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_remove_article_publication_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='edicion',
            new_name='edition',
        ),
    ]
