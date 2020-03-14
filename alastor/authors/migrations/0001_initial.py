# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Nombre')),
                ('photo', models.ImageField(blank=True, upload_to='author', verbose_name='Foto')),
            ],
        ),
    ]
