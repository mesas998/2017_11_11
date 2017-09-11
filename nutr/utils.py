from django.shortcuts import get_object_or_404, redirect, render
from .models import POC, Tag, NewsLink
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.db import IntegrityError
from django.core.urlresolvers import reverse_lazy
import sys

class PageLinksMixin:
    page_kwarg = 'page'

    def _page_urls(self, page_number):
        return "?{pkw}={n}".format(
            pkw=self.page_kwarg,
            n=page_number)

    def first_page(self, page):
        # don't show on first page
        if page.number > 1:
            return self._page_urls(1)
        return None

    def previous_page(self, page):
        if (page.has_previous()
                and page.number > 2):
            return self._page_urls(
                page.previous_page_number())
        return None

    def next_page(self, page):
        last_page = page.paginator.num_pages
        if (page.has_next()
                and page.number < last_page - 1):
            return self._page_urls(
                page.next_page_number())
        return None

    def last_page(self, page):
        last_page = page.paginator.num_pages
        if page.number < last_page:
            return self._page_urls(last_page)
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs)
        page = context.get('page_obj')
        if page is not None:
            context.update({
                'first_page_url':
                    self.first_page(page),
                'previous_page_url':
                    self.previous_page(page),
                'next_page_url':
                    self.next_page(page),
                'last_page_url':
                    self.last_page(page),
            })
        return context


class NutDataContextMixin():
    nutdata_ndb_no_url_kwarg = 'nutdata_ndb_no'
    nutdata_context_object_name = 'nutdata'

    def get_context_data(self, **kwargs):
        if hasattr(self, 'nutdata'):
            context = {
                self.nutdata_context_object_name:
                    self.nutdata,
            }
        else:
            nutdata_ndb_no = self.kwargs.get(
                self.nutdata_ndb_no_url_kwarg)
            nutdata = get_object_or_404(
                NutData,
                ndb_no__iexact=nutdata_ndb_no)
            context = {
                self.nutdata_context_object_name:
                    nutdata,
            }
        context.update(kwargs)
        return super().get_context_data(**context)


"""
# replaced (below) 7/24/17
class POCContextMixin():
    poc_slug_url_kwarg = 'poc_slug'
    poc_context_object_name = 'poc'

    def get_context_data(self, **kwargs):
        if hasattr(self, 'poc'):
            context = {
                self.poc_context_object_name:
                    self.poc,
            }
        else:
            poc_pk = self.kwargs.get( self.poc_pk_url_kwarg)
            poc=POC.objects.get(pk=8597)
            context = { self.poc_context_object_name: poc, }
        context.update(kwargs)
        return super().get_context_data(**context)
"""
class POCContextMixin():
    poc_slug_url_kwarg = 'poc_slug'
    poc_context_object_name = 'poc'

    def get_context_data(self, **kwargs):
        if hasattr(self, 'poc'):
            context = {
                self.poc_context_object_name:
                    self.poc,
            }
        else:
            poc_slug = self.kwargs.get(
                self.poc_slug_url_kwarg)
            poc = get_object_or_404(
                POC,
                slug__iexact=poc_slug)
            context = {
                self.poc_context_object_name:
                    poc,
            }
        context.update(kwargs)
        return super().get_context_data(**context)

class ObjectCreateMixin:
    print('ObjectCreateMixin (73)')
    form_class = None
    template_name = ''
    #ancel_url = reverse_lazy('nutr_poc_list')

    def get(self, request):
        print('ObjectCreateMixin (77)')
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def post(self, request):
        print('ObjectCreateMixin (79b)')
        bound_form = self.form_class(request.POST)
        print('ObjectCreateMixin (79e)')
        if "cancel" in request.POST:
            print('ObjectCreateMixin (79h)')
            return HttpResponseRedirect(reverse_lazy('nutr_poc_list'))
        if bound_form.is_valid():
            print('ObjectCreateMixin (79s)')
            try:
                print('ObjectCreateMixin (79t)')
                new_object = bound_form.save()
                print('ObjectCreateMixin (79u)')
                return redirect(new_object)
            except IntegrityError as e:
                print('ObjectCreateMixin (79v)')
                #TODO: should redirect to tha country with error message:
                #eturn HttpResponse("ERROR: Object already exists!")
                print('ObjectCreateMixin (79w): ',e.args)
                #eturn render_to_response(self.template_name, {"message": e.args})
                return render_to_response(self.template_name, {"message": self.error_friendly(str(sys.exc_info()[1]))} )
            except Error as err:
                print('ObjectCreateMixin (79y) '+sys.exec_info()[0])
        else:
            print('ObjectCreateMixin (79x)')
            return render(
                request,
                self.template_name,
                {'form': bound_form})
    def error_friendly(self,s):
        try:
            first = s.index('DETAIL:')+7
            msg=s[first:]
            return msg
        except:
            return s

class ObjectDeleteMixin:
    model = None
    success_url = ''
    template_name = ''

    def get(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug)
        context = {
            self.model.__name__.lower(): obj,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug)
        obj.delete()
        return HttpResponseRedirect(
            self.success_url)

class ObjectUpdateMixin:
    form_class = None
    model = None
    template_name = ''

    def get(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug)
        context = {
            'form': self.form_class(instance=obj),
            self.model.__name__.lower(): obj,
            'pk':obj.pk,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, slug):
        obj = get_object_or_404(
            self.model, slug__iexact=slug)
        bound_form = self.form_class(
            request.POST, instance=obj)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            context = {
                'form': bound_form,
                self.model.__name__.lower(): obj,
            }
            return render(
                request,
                self.template_name,
                context)

class AutoSlugMixin(object):
    _slug_from = 'name'
    _slug_field = 'slug'

    def slugify(self, name):
        return slugify(name)

    def generate_slug(self):
        name = getattr(self, self._slug_from)
        return self.slugify(name)

    def update_slug(self, commit=True):
        if not getattr(self, self._slug_field) and \
               getattr(self, self._slug_from):
            setattr(self, self._slug_field, self.generate_slug())

            if commit:
                self.save()

class NewsLinkGetObjectMixin():
    def get_object(self, queryset=None):
        poc_slug = self.kwargs.get(
            self.poc_slug_url_kwarg)
        newslink_slug = self.kwargs.get(
            self.slug_url_kwarg)
        return get_object_or_404(
            NewsLink,
            slug__iexact=newslink_slug,
            poc__slug__iexact=poc_slug)

