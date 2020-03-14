# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import AuthorDetailView


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', AuthorDetailView.as_view(), name='detail'),
]
