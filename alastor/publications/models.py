from __future__ import unicode_literals
# -*- coding: utf-8 -*-

from django.db import models
from alastor.authors.models import Author


class Publication(models.Model):
    name = models.CharField(max_length=140, verbose_name=u'Nombre')
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
    promoted = models.BooleanField('Promocionar', default=False)

    class Meta:
        verbose_name = u'Libro'
        verbose_name_plural = u'Libros'
        ordering = ('-id', )

    def __str__(self):
        return self.name
