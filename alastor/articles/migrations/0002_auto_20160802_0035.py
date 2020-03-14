# -*- coding: utf-8 -*-

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='articles.Section'),
            preserve_default=False,
        ),
    ]
