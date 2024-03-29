from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.contrib import admin
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_select2.forms import Select2Widget

from alastor.articles.models import Article, Section, ImageArticle


class PageForm(FlatpageForm):
    class Meta:
        fields = '__all__'
        model = FlatPage
        widgets = {
            'content': CKEditorUploadingWidget,
        }


class PageAdmin(FlatPageAdmin):
    form = PageForm


class ArticleForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Article
        widgets = {
            'author': Select2Widget,
            'translator': Select2Widget,
            'body': CKEditorUploadingWidget,
            'translation_body': CKEditorUploadingWidget,
            'introduction': CKEditorUploadingWidget,
            'image_caption': CKEditorUploadingWidget
        }


class ImageArticleInline(admin.StackedInline):
    model = ImageArticle
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'section', 'edition', 'hide')
    inlines = [ImageArticleInline, ]
    fieldsets = (
        ('Texto', {'fields': ('title', 'slug', 'introduction', 'body',)}),
        ('Traduccion', {'fields': ('is_translation', 'translation_body', 'translator')}),
        ('Detalles', {'fields': ('hide', 'section', 'author', 'edition', 'image', 'image_caption')})
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Section)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
