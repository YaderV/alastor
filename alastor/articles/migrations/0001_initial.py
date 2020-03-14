# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='T\xedtulo')),
                ('publication_date', models.DateField(blank=True, null=True, verbose_name='Fecha de publicaci\xf3n')),
                ('introduction', models.TextField(blank=True, verbose_name='Introducci\xf3n/Entradilla')),
                ('body', models.TextField(verbose_name='Texto')),
            ],
        ),
    ]
