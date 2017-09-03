from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import HiddenInput
from .models import POC, Tag, NewsLink, Document
from django.utils.translation import gettext, ugettext_lazy as _


class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    """
    def clean_slug(self):
        new_slug = (
            self.cleaned_data['name'].lower())
        if new_slug == 'create':
            raise ValidationError(
                'Slug may not be "create".')
        return new_slug
    def clean(self):
        #leaned_data = super(POCForm, self)
        name = self.cleaned_data['name']
        slug = self.cleaned_data['name'].lower()
        self.cleaned_data['slug']=slug
        # do your cleaning here
        return self.cleaned_data
    """

"""
# notice this is commented out 
# let's try a 101 version before we move everything behind a curtain (this is TagForm example p.193:
class POCForm(forms.Form):
    name = forms.CharField(max_length=31)
    slug = forms.SlugField( max_length=31, help_text='A label for URL config')
    tag = forms.ModelChoiceField(queryset=Tag.objects.all())

"""
# final version chapter 9:
class POCForm( SlugCleanMixin, forms.ModelForm):
    #ame = forms.CharField(max_length=31)
    #ag = forms.ModelChoiceField(queryset=Tag.objects.all())
    #gmage = forms.FileField()
    #ESNO_CHOICES = ((0, 'No'), (1, 'Yes'))
    #mnesty = forms.ChoiceField( choices=YESNO_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = POC
        #ields = '__all__'
        exclude = ['slug','image','created_date', 'updated_date']


class TagForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        #eturn self.cleaned_data['name'].lower()
        return self.cleaned_data['name']

class NewsLinkForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = NewsLink
        #ields = '__all__'
        exclude = ['slug']
        widgets={'poc':HiddenInput()}

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
