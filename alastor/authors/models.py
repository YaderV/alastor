# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=140, verbose_name=u'Nombre')
    photo = models.ImageField(upload_to='author', blank=True,
                              verbose_name=u'Foto')
    bio = models.TextField(blank=True, verbose_name=u'Biografía')
    promote = models.BooleanField(
        default=False, verbose_name=u'Promover',
        help_text=u'Promover autor como autor destacado en index'
    )

    class Meta:
        verbose_name = u'Autor'
        verbose_name_plural = u'Autores'
        ordering = ['-promote', 'name']

    def __str__(self):
        return self.name
