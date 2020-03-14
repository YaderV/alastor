from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget
from .models import Publication


class PublicationForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Publication
        widgets = {
            'description': CKEditorWidget
        }


class PublicationAdmin(admin.ModelAdmin):
    form = PublicationForm

admin.site.register(Publication, PublicationAdmin)
