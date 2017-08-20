from django.core.paginator import ( EmptyPage, PageNotAnInteger, Paginator)
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.views.generic import ( CreateView, DeleteView, DetailView, ListView)


from .forms import TagForm, POCForm, NewsLinkForm
from .models import Tag, POC, NewsLink
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin, POCContextMixin
from .utils import PageLinksMixin, NutDataContextMixin, POCContextMixin, NewsLinkGetObjectMixin

from django.http.response import HttpResponse
from django.template import Context, loader
from core.utils import UpdateView
from user.decorators import class_login_required, require_authenticated_permission
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
#mport requests
from django.core.paginator import Paginator
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import LoginRequiredMixin

"""
class POCList(View):
    page_kwarg = 'page'
    paginate_by = 5  # 5 items per page
    template_name = 'nutr/poc_list.html'

    def get(self, request):
        poc = POC.objects.all()
        paginator = Paginator(
            poc, self.paginate_by)
        page_number = request.GET.get(
            self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated':page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'poc_list': page,
        }
        return render(
            request, self.template_name, context)
"""

class POCList(PageLinksMixin, ListView):
    model = POC
    paginate_by = 30

def poc_detail(request, slug):
    poc = get_object_or_404(
        POC, slug=slug)
    return render(
        request,
        'nutr/poc_detail.html',
        {'poc': poc 
	#poc.image': poc.image.url
        })

def homepage(request):
    return render(
        request,
        'nutr/tag_list.html',
        {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    return render(
        request,
        'nutr/tag_detail.html',
        {'tag': tag})

def image(request, jpg):
    #eturn HttpResponse(jpg)
    return render(
        request,
        jpg,
        {})

class TagList(PageLinksMixin, ListView):
    paginate_by = 300
    model = Tag


def poc_create(request):
    if request.method == 'POST':
        form = POCForm(request.POST)
        if form.is_valid():
            new_poc = form.save()
            return redirect(new_poc)
    else:  # request.method != 'POST'
        form = POCForm()
    return render(
        request,
        'nutr/poc_form.html',
        {'form': form})

#require_authenticated_permission( 'nutr.create_poc')
class POCCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_class = POCForm
    template_name = 'nutr/poc_form.html'

@require_authenticated_permission(
    'nutr.create_tag')
class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'nutr/tag_form.html'

@require_authenticated_permission(
    'nutr.update_tag')
class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name = (
        'nutr/tag_form_update.html')

@require_authenticated_permission(
    'nutr.delete_tag')
class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    success_url = reverse_lazy(
        'nutr_tag_list')
    template_name = (
        'nutr/tag_confirm_delete.html')

@require_authenticated_permission(
    'nutr.update_poc')
class POCUpdate(ObjectUpdateMixin, View):
    form_class = POCForm
    model = POC
    template_name = (
        'nutr/poc_form_update.html')

@require_authenticated_permission(
    'nutr.delete_poc')
class POCDelete(ObjectDeleteMixin, View):
    model = POC
    success_url = reverse_lazy(
        'nutr_poc_list')
    template_name = (
        'nutr/poc_confirm_delete.html')

class NewsLinkCreate(
        NewsLinkGetObjectMixin,
        POCContextMixin,
        CreateView):
    form_class = NewsLinkForm
    model = NewsLink

    def get_initial(self):
        poc_slug = self.kwargs.get(
            self.poc_slug_url_kwarg)
        self.poc = get_object_or_404(
            POC, slug__iexact=poc_slug)
        initial = {
            self.poc_context_object_name:
                self.poc,
        }
        initial.update(self.initial)
        return initial

class NewsLinkDelete(
        NewsLinkGetObjectMixin,
        POCContextMixin,
        DeleteView):
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'

    def get_success_url(self):
        return (self.object.poc
                .get_absolute_url())


class NewsLinkUpdate(
        NewsLinkGetObjectMixin,
        POCContextMixin,
        UpdateView):
    form_class = NewsLinkForm
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'


def upload(request):
    print('upload() (21)')
    if request.method == 'POST' and request.FILES['myfile']:
        print('upload() (22)')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        print('upload() (26)')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print('upload() (27)')
        return render(request, 'nutr/poc_image_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    print('upload() (28)')
    return render(request, 'nutr/poc_image_upload.html')

def upload_do(request,slug):
    print('upload_do() (2)')
    return HttpResponse()

def simple_upload(request):
    print('simple_upload() (1)')
    if request.method == 'POST' and request.FILES['myfile']:

        print('simple_upload() (2)')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        print('simple_upload() (6)')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print('simple_upload() (9)')
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'nutr/tag_list.html')


def model_form_upload(request):
    print('model_form_upload() (1)')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
