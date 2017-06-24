from django.core.paginator import ( EmptyPage, PageNotAnInteger, Paginator)
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.views.generic import ( CreateView, DeleteView, DetailView, ListView)

from .forms import NewsLinkForm
from .models import NewsLink, Tag, POC
from .utils import NewsLinkGetObjectMixin, PageLinksMixin, POCContextMixin
from django.http.response import HttpResponse
from django.template import Context, loader
from .utils import ( PageLinksMixin, NutDataContextMixin)
from django.views.generic import ( CreateView, DeleteView, DetailView, ListView)
from core.utils import UpdateView
from user.decorators import class_login_required, require_authenticated_permission
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
#mport requests
from django.core.paginator import Paginator
from django.views.generic import View

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

def poc_detail(request, pk):
    poc = get_object_or_404(
        POC, pk=pk)
    return render(
        request,
        'nutr/poc_detail.html',
        {'poc': poc, 'poc.image': poc.image.url})

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

"""
def tag_list(request):
    return render(
        request,
        'nutr/tag_list.html',
        {'tag_list': Tag.objects.all()})
"""
class TagList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Tag
