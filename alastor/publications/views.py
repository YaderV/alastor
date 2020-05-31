from django.views.generic import ListView, DetailView
from .models import Publication


class PublicationList(ListView):
    model = Publication
    template_name = 'publications/list.html'
    context_object_name = 'publications'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publication_flag'] = True

        return context


class PublicationDetailView(DetailView):
    model = Publication
    context_object_name = 'publication'
    template_name = 'publications/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publication_flag'] = True
        return context
