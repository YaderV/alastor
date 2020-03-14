# -*- coding: utf-8 -*-

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0005_auto_20170116_1753'),
        ('editions', '0008_edition_draft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Nombre')),
                ('archivo', models.FileField(upload_to='publication', verbose_name='Archivo')),
                ('description', models.TextField(blank=True, verbose_name='Descripci\xf3n')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Author', verbose_name='Autor')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editions.Edition', verbose_name='Edici\xf3n')),
            ],
            options={
                'verbose_name': 'Publicaci\xf3n',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
    ]
