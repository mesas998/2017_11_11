from django.shortcuts import get_object_or_404, redirect, render
from .models import POC, Tag, NewsLink
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.db import IntegrityError
from django.core.urlresolvers import reverse_lazy
import sys
import logging
#ogger = logging.getLogger(__name__)


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
    logging.info('ObjectCreateMixin (73) - this is a logging.info')
    #rint('ObjectCreateMixin (73) - this is a print')
    form_class = None
    template_name = ''
    #ancel_url = reverse_lazy('nutr_poc_list')

    def get(self, request):
        logging.debug('ObjectCreateMixin (77)')
        return render(
            request,
            self.template_name,
            {'form': self.form_class()})

    def post(self, request):
        logging.info('ObjectCreateMixin (79a) -  this is a logging.debug with heroku (should get filtered out)')
        #rint('ObjectCreateMixin (79a) -  this is a print')
        bound_form = self.form_class(request.POST)
        logging.debug('ObjectCreateMixin (79e)')
        if "cancel" in request.POST:
            logging.debug('ObjectCreateMixin (79h)')
            return HttpResponseRedirect(reverse_lazy('nutr_tag_list'))
        if bound_form.is_valid():
            logging.debug('ObjectCreateMixin (79s)')
            try:
                logging.debug('ObjectCreateMixin (79t)')
                new_object = bound_form.save()
                logging.info('ObjectCreateMixin (79u) new_object created: '+str(new_object.pk)+' '+new_object.name)
                #rint('ObjectCreateMixin (79u) new_object created: '+str(new_object.pk)+' '+new_object.name)
                return redirect(new_object)
            except IntegrityError as e:
                #TODO: should redirect to tha country with error message:
                #eturn HttpResponse("ERROR: Object already exists!")
                logging.warning('ObjectCreateMixin (79w) IntegrityError: ',e.args)
                #rint('ObjectCreateMixin (79w) IntegrityError: ',e.args)
                #eturn render_to_response(self.template_name, {"message": e.args})
                return render_to_response(self.template_name, {"message": self.error_friendly(str(sys.exc_info()[1]))} )
            except Exception as err:
                logging.warning('ObjectCreateMixin (79y) '+str(err))
                #rint('ObjectCreateMixin (79y) '+str(err))
                return render_to_response(self.template_name, {"message": self.error_friendly(str(sys.exc_info()[1]))} )
        else:
            logging.info('ObjectCreateMixin (79x)')
            #rint('ObjectCreateMixin (79x)')
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
        logging.info('ObjectDeleteMixin (73m) attempting to delete '+str(obj.pk)+' '+obj.name)
        #rint('ObjectDeleteMixin (73m) attempting to delete '+str(obj.pk)+' '+obj.name)
        obj.delete()
        logging.info('ObjectDeleteMixin (73p) delete appears to have succeeded')
        #rint('ObjectDeleteMixin (73p) delete appears to have succeeded')
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
        logging.info('ObjectUpdateMixin (71m) attempting to update '+str(obj.pk)+' '+obj.name)
        #rint('ObjectUpdateMixin (71m) attempting to update '+str(obj.pk)+' '+obj.name)
        #rint('ObjectUpdateMixin (71o) - self.request.user: '+str(self.request.user))
        bound_form = self.form_class(
            request.POST, instance=obj)
        if bound_form.is_valid():
            logging.info('ObjectUpdateMixin (71r) form is valid - proceeding with update')
            #rint('ObjectUpdateMixin (71r) form is valid - proceeding with update')
            new_object = bound_form.save()
            return redirect(new_object)
        else:
            logging.info('ObjectUpdateMixin (71t) form is not valid')
            #rint('ObjectUpdateMixin (71t) form is not valid')
            context = {
                'form': bound_form,
                self.model.__name__.lower(): obj,
            }
            logging.info('ObjectUpdateMixin (71w) - context: ')
            #rint('ObjectUpdateMixin (71w) - context: ')
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

