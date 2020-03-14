# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Nombre')),
                ('slug', models.SlugField(unique=True)),
                ('cover', models.ImageField(blank=True, upload_to='edition', verbose_name='Portada')),
            ],
            options={
                'verbose_name': 'Edici\xf3n',
                'verbose_name_plural': 'Ediciones',
            },
        ),
    ]
