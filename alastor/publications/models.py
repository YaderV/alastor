# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from alastor.editions.models import Edition
from alastor.authors.models import Author


class Publication(models.Model):
    name = models.CharField(max_length=140, verbose_name=u'Nombre')
    edition = models.ForeignKey(
        Edition, verbose_name=u'Edición',
        on_delete=models.CASCADE
    )
    cover = models.ImageField(upload_to='cover', blank=True,
                              verbose_name=u'Portada')
    author = models.ForeignKey(
        Author, verbose_name=u'Autor',
        on_delete=models.CASCADE
    )
    archivo = models.FileField(upload_to='publication',
                               verbose_name=u'Archivo')
    description = models.TextField(verbose_name=u'Descripción',
                                   blank=True)

    class Meta:
        verbose_name = u'Libro'
        verbose_name_plural = u'Libros'
        ordering = ('-edition__number', )

    def __str__(self):
        return self.name
