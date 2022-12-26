# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.decorators.cache import cache_page
from .views import ArticleListEditionView, ArticleListView, \
    SectionListView, ArticleDetailView, TestArticleListView


urlpatterns = [
    url(r'^$',
        cache_page(60 * 60)(ArticleListView.as_view()),
        name='index'),
    url(r'^test/$', TestArticleListView.as_view(), name='test-index'),
    url(r'^seccion/(?P<slug>[-\w]+)/$',
        cache_page(60 * 60)(SectionListView.as_view()),
        name='section'),
    url(r'^edicion/(?P<number>[-\w]+)/$',
        cache_page(60 * 60)(ArticleListEditionView.as_view()),
        name='edition'),
    url(r'^articulo/(?P<slug>[-\w]+)/$',
        ArticleDetailView.as_view(), name='detail')
]
