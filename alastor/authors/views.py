from django.views.generic import DetailView, ListView
from .models import Author


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'authors/detail.html'

    def get_queryset(self):
        qs = super(AuthorDetailView, self).get_queryset()
        return qs.prefetch_related('article_set')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_flag'] = True
        return context


class AuthoListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'authors/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors_promoted'] = context['authors'].filter(
            promote=True)

        context['authors'] = context['authors'].exclude(
            promote=True)
        context['author_flag'] = True
        return context
