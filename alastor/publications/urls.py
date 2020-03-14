# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PublicationList


urlpatterns = [
    url(r'^$', PublicationList.as_view(), name='index'),
]
