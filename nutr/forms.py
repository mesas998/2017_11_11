from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput
from .models import POC, NewsLink


class SlugCleanMixin:
    """Mixin class for slug cleaning method."""
    def clean_slug(self):
        new_slug = (
            self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError(
                'Slug may not be "create".')
        return new_slug

class NewsLinkForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'
        widgets = {'startup': HiddenInput()}

class POCForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = POC
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()
