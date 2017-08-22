from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, ArchiveIndexView, CreateView, DeleteView, DetailView, MonthArchiveView, YearArchiveView
from django.shortcuts import get_object_or_404, redirect, render

from core.utils import UpdateView
from user.decorators import \
    require_authenticated_permission

from .forms import PostForm
from .models import Post
from .utils import ( AllowFuturePermissionMixin, DateObjectMixin, PostFormValidMixin)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class PostArchiveMonth(
        AllowFuturePermissionMixin,
        MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


class PostArchiveYear(
        AllowFuturePermissionMixin,
        YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True


#require_authenticated_permission( 'blog.add_post')
class PostCreate(LoginRequiredMixin, PostFormValidMixin, CreateView):
    form_class = PostForm
    model = Post


#require_authenticated_permission( 'blog.delete_post')
class PostDelete(LoginRequiredMixin, DateObjectMixin, DeleteView):
    date_field = 'pub_date'
    model = Post
    #uccess_url = reverse_lazy('blog_post_list')
    success_url = reverse_lazy('nutr_poc_list')


class PostDetail(DateObjectMixin, DetailView):
    date_field = 'pub_date'
    model = Post


class PostList(
        AllowFuturePermissionMixin,
        ArchiveIndexView):
    allow_empty = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'


#require_authenticated_permission( 'blog.change_post')
class PostUpdate( LoginRequiredMixin, PostFormValidMixin, DateObjectMixin,
        UpdateView):
    date_field = 'pub_date'
    form_class = PostForm
    model = Post

