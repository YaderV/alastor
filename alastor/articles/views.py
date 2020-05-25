from django.views.generic import ListView, DetailView
from django.db.models import Count
from django.shortcuts import redirect
from alastor.editions.models import Edition
from alastor.publications.models import Publication
from .models import Article, Section, Author


class ArticleBaseView(ListView):
    model = Article
    template_name = 'articles/list.html'
    author_list = None

    def dispatch(self, request, *args, **kwargs):
        self.author_list = Author.objects.annotate(
            art_count=Count('article')).filter(art_count__gt=0)
        return super(ArticleBaseView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(ArticleBaseView, self).get_queryset()
        return qs.select_related('author')

    def get_context_data(self, **kwargs):
        context = super(ArticleBaseView, self).get_context_data(**kwargs)
        context['editions'] = Edition.objects.exclude(draft=True)
        for section in Section.objects.all():
            context.update({
                section.slug: context['object_list'].filter(section=section)
            })

        return context


class ArticleListView(ArticleBaseView):
    edition = None

    def get_queryset(self):
        qs = super(ArticleListView, self).get_queryset()
        # TODO Write an accurate way to get latest edition
        self.edition = Edition.objects.exclude(draft=True).first()
        return qs.filter(edition=self.edition)

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['author_list'] = self.author_list.filter(article__edition=self.edition)
        # context['author_old'] = self.author_list.exclude(article__edition=self.edition)
        context['books'] = Publication.objects.filter(promoted=True)[:4]
        return context


class ArticleListEditionView(ArticleBaseView):

    def dispatch(self, request, *args, **kwargs):
        is_draft = Edition.objects.filter(
            number=self.kwargs['number'], draft=True).exists()
        if is_draft and not request.user.is_authenticated():
            return redirect('articles:index')
        return super(ArticleListEditionView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(ArticleListEditionView, self).get_queryset()
        return qs.filter(edition__number=self.kwargs['number'])

    def get_context_data(self, **kwargs):
        context = super(ArticleListEditionView, self).get_context_data(**kwargs)
        context['author_list'] = self.author_list.filter(
            article__edition__number=self.kwargs['number'])
        context['author_old'] = self.author_list.exclude(
            article__edition__number=self.kwargs['number'])
        return context


class SectionListView(ListView):
    model = Article
    template_name = 'articles/section.html'
    context_object_name = 'articles'

    def get_queryset(self):
        qs = super(SectionListView, self).get_queryset()
        return qs.filter(section__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(SectionListView, self).get_context_data(**kwargs)
        context['editions'] = Edition.objects.exclude(draft=True)
        # TODO Write an accurate way to get latest edition
        edition = Edition.objects.exclude(draft=True).first()
        context['edition_articles'] = context['articles'].select_related(
            'author').filter(edition=edition)
        context['old_articles'] = context['articles'].exclude(
            edition=edition).filter(edition__draft=False)

        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'

    def dispatch(self, request, *args, **kwargs):
        is_draft = self.get_object().edition.draft
        if is_draft and not request.user.is_authenticated():
            return redirect('articles:index')
        return super(ArticleDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_articles'] = self.model.objects.exclude(
            id=self.object.id).order_by('?')[:3]
        return context
