# Generated by Django 2.2 on 2023-01-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20180730_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hide',
            field=models.BooleanField(default=False, verbose_name='Ocultar'),
        ),
    ]
