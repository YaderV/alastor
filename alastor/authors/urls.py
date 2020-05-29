# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import AuthorDetailView, AuthoListView


urlpatterns = [
    url(r'^$', AuthoListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', AuthorDetailView.as_view(), name='detail'),
]
