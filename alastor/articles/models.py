from django.urls import reverse
from django.db import models

from alastor.authors.models import Author
from alastor.editions.models import Edition


class Section(models.Model):
    name = models.CharField(max_length=140, verbose_name=u'Nombre')
    slug = models.SlugField(unique=True, verbose_name=u'Link de enlace')

    def get_absolute_url(self):
        return reverse('articles:section', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = u'Sección'
        verbose_name_plural = u'Secciones'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=140, verbose_name=u'Título')
    slug = models.SlugField(unique=True, verbose_name=u'Link de enlace')

    introduction = models.TextField(
        blank=True, verbose_name=u'Introducción/Entradilla')
    body = models.TextField(verbose_name=u'Texto')
    is_translation = models.BooleanField(
        verbose_name=u'Traducción', default=False)
    translation_body = models.TextField(
        blank=True, verbose_name=u'Texto traducido')
    translator = models.ForeignKey(
        Author,
        verbose_name=u'Traductor', null=True,
        blank=True, related_name='article_translator',
        on_delete=models.CASCADE
    )
    section = models.ForeignKey(
        Section, verbose_name=u'Sección',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        Author, verbose_name=u'Autor',
        on_delete=models.CASCADE
    )
    edition = models.ForeignKey(
        Edition, verbose_name=u'Edición',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='article', blank=True,
                              verbose_name=u'Imagen de texto')
    image_caption = models.TextField(
        blank=True, verbose_name=u'Descripción de imagen'
    )

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = u'Artículo'
        verbose_name_plural = u'Artículos'

    def __str__(self):
        return self.title


class ImageArticle(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='article',
                              verbose_name=u'Imagen de galería')
    image_caption = models.TextField(
        blank=True, verbose_name=u'Descripción de imagen'
    )

    class Meta:
        verbose_name = u'Imagen de galería'
        verbose_name_plural = u'Imagenes de galería'

    def __str__(self):
        return "{} - {}".format(self.article, self.pk)
