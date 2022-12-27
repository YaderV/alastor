# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Edition(models.Model):
    number = models.PositiveIntegerField(verbose_name=u'Número', unique=True)
    publication_date = models.DateField(
        verbose_name=u'Fecha de edición',
        null=True,
        blank=True
    )
    cover = models.ImageField(upload_to='edition', blank=True,
                              verbose_name=u'Portada')

    draft = models.BooleanField(verbose_name='Borrador', default=True)

    class Meta:
        ordering = ('-number',)
        verbose_name = u'Edición'
        verbose_name_plural = u'Ediciones'
        app_label = 'editions'

    def get_date(self):
        return self.publication_date.strftime('%b %Y')

    def get_absolute_url(self):
        return reverse('articles:edition', kwargs={'number': self.number})

    def __str__(self):
        return '{0} - {1}'.format(
            self.number,
            self.get_date()
        )
