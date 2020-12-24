from collections import defaultdict
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from alastor.editions.models import Edition
from alastor.publications.models import Publication
from .models import Article, Section, Author


class ArticleBaseView(ListView):
    model = Article
    template_name = 'articles/list.html'
    author_list = None
    edition_list = None
    current_edition = None

    def get_queryset(self):
        qs = super(ArticleBaseView, self).get_queryset()
        self.edition_list = Edition.objects.exclude(draft=True)

        if 'number' in self.kwargs:
            self.current_edition = self.edition_list.get(
                number=self.kwargs['number']
            )
        else:
            self.current_edition = self.edition_list.first()

        qs = qs.filter(edition=self.current_edition).select_related(
            'author', 'section'
        ).order_by('section')
        self.author_list = Author.objects.filter(
            article__in=qs).distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super(ArticleBaseView, self).get_context_data(**kwargs)
        context['editions'] = self.edition_list
        context['index_flag'] = True
        context['author_list'] = self.author_list
        context['edition'] = self.current_edition

        articles = defaultdict(list)
        for i in context['article_list']:
            articles[i.section.name].append(i)

        context['articles'] = articles.items()

        return context


class ArticleListView(ArticleBaseView):

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['books'] = Publication.objects.filter(
            promoted=True).select_related('author')[:4]
        return context


class ArticleListEditionView(ArticleBaseView):
    pass


class TestArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    author_list = None
    edition_list = None
    current_edition = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('articles:index')
        return super(TestArticleListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(TestArticleListView, self).get_queryset()
        self.edition_list = Edition.objects.all()

        if 'number' in self.kwargs:
            self.current_edition = self.edition_list.get(
                number=self.kwargs['number']
            )
        else:
            self.current_edition = self.edition_list.first()

        qs = qs.filter(edition=self.current_edition).select_related(
            'author', 'section'
        ).order_by('section')
        self.author_list = Author.objects.filter(
            article__in=qs).distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super(TestArticleListView, self).get_context_data(**kwargs)
        context['editions'] = self.edition_list
        context['index_flag'] = True
        context['author_list'] = self.author_list
        context['edition'] = self.current_edition

        articles = defaultdict(list)
        for i in context['article_list']:
            articles[i.section.name].append(i)

        context['articles'] = articles.items()

        return context


class SectionListView(ListView):
    model = Article
    template_name = 'articles/section.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        qs = super(SectionListView, self).get_queryset()
        self.edition = Edition.objects.exclude(draft=True).first()
        qs = qs.exclude(
            section__slug=self.kwargs['slug'],
            edition__draft=True,
            edition=self.edition
        ).select_related('author')
        return qs

    def get_context_data(self, **kwargs):
        context = super(SectionListView, self).get_context_data(**kwargs)
        context['editions'] = Edition.objects.exclude(draft=True)
        # TODO Write an accurate way to get latest edition
        context['edition_articles'] = self.model.objects.filter(
            section__slug=self.kwargs['slug'],
            edition=self.edition
        ).select_related('author')
        context['section'] = Section.objects.get(
            slug=self.kwargs['slug'])

        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'

    def dispatch(self, request, *args, **kwargs):
        is_draft = self.get_object().edition.draft
        if is_draft and not request.user.is_authenticated:
            return redirect('articles:index')
        return super(ArticleDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_articles'] = self.model.objects.exclude(
            id=self.object.id).order_by('?')[:3]
        return context
