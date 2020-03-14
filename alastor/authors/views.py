from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'authors/detail.html'

    def get_queryset(self):
        qs = super(AuthorDetailView, self).get_queryset()
        return qs.prefetch_related('article_set')
