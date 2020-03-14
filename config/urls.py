# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
# from django.contrib.flatpages import views as flatpage_views

urlpatterns = [
    url(r'^', include(('alastor.articles.urls', 'articles'),
        namespace='articles')),
    url(r'^autor/', include(('alastor.authors.urls', 'authors'),
        namespace='authors')),
    url(r'^publicaciones/',
        include(('alastor.publications.urls', 'publications'),
                namespace='publications')),
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^ckeditor/', include(
        ('ckeditor_uploader.urls', 'ckeditor_uploader'))),
    url(r'^select2/', include(
        ('django_select2.urls', 'django_select2'))),

    # Your stuff: custom urls includes go here

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    import debug_toolbar
    urlpatterns += [
        # url(r'^presentacion/$', flatpage_views.flatpage, {'url': '/presentacion/'}, name='presentation'),
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
