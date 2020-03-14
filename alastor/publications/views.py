from django.views.generic import ListView
from .models import Publication


class PublicationList(ListView):
    model = Publication
    template_name = 'publications/list.html'
    context_object_name = 'publications'

    def get_queryset(self):
        qs = super(PublicationList, self).get_queryset()
        return qs.filter(edition__draft=False)
