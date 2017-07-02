from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput
from .models import POC, NewsLink, Tag


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

# let's try a 101 version before we move everything behind a curtain (this is TagForm example p.193:
class POCForm(forms.Form):
    name = forms.CharField(max_length=31)
    slug = forms.SlugField(
        max_length=31,
        help_text='A label for URL config')

    def save(self):
        new_poc = POC.objects.create(
            name=self.cleaned_data['name'],
            slug=self.cleaned_data['slug'])
        return new_poc

"""
# final version chapter 9:
class POCForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = POC
        fields = ['name','slug']
"""


class TagForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        #eturn self.cleaned_data['name'].lower()
        return self.cleaned_data['name']
