from django import forms
from django.contrib import admin

from ckeditor.widgets import CKEditorWidget
from alastor.authors.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Author
        widgets = {
            'bio': CKEditorWidget
        }


class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm


admin.site.register(Author, AuthorAdmin)
