# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ('-edition__number',), 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.AddField(
            model_name='publication',
            name='cover',
            field=models.ImageField(blank=True, upload_to='cover', verbose_name='Portada'),
        ),
    ]
