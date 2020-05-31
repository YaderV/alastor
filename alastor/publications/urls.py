# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import PublicationList, PublicationDetailView


urlpatterns = [
    url(
        r'^$',
        PublicationList.as_view(),
        name='index'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        PublicationDetailView.as_view(),
        name='detail'
    ),
]
