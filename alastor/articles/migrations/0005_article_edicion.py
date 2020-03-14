# -*- coding: utf-8 -*-

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editions', '0004_edition_publication_date'),
        ('articles', '0004_auto_20160802_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='edicion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='editions.Edition'),
            preserve_default=False,
        ),
    ]
