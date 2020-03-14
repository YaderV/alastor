# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import ArticleListEditionView, ArticleListView, \
    SectionListView, ArticleDetailView


urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='index'),
    url(r'^seccion/(?P<slug>[-\w]+)/$',
        SectionListView.as_view(), name='section'),
    url(r'^edicion/(?P<number>[-\w]+)/$',
        ArticleListEditionView.as_view(), name='edition'),
    url(r'^articulo/(?P<slug>[-\w]+)/$',
        ArticleDetailView.as_view(), name='detail')
]
