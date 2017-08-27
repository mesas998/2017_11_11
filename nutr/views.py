from django.core.paginator import ( EmptyPage, PageNotAnInteger, Paginator)
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.views.generic import ( CreateView, DeleteView, DetailView, ListView)
from .forms import TagForm, POCForm, NewsLinkForm
from .models import Tag, POC, NewsLink
from .utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin, POCContextMixin
from .utils import PageLinksMixin, NutDataContextMixin, POCContextMixin, NewsLinkGetObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
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
import cloudinary
import cloudinary.uploader
import cloudinary.api
import unicodedata

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
    name=poc.name
    print('51a type(name): ',type(name))
    #lone2 =''.join(e for e in name if e.isalpha())
    #rint('51e type(clone2): ',type(clone2))
    clone3=strip_accents3(name)
    jpg_url="http://res.cloudinary.com/hh9sjfv1s/image/upload/v1503419459/"+clone3+".jpg"
    jpg_url=jpg_url.replace(' ','_')
    print('(51p) jpg_url: ',jpg_url)
    return render(
        request,
        'nutr/poc_detail.html',
        {'poc': poc ,
        'jpg_url':jpg_url,
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

class POCCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_class = POCForm
    template_name = 'nutr/poc_form.html'

@require_authenticated_permission( 'nutr.create_tag')
class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'nutr/tag_form.html'

@require_authenticated_permission( 'nutr.update_tag')
class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name = (
        'nutr/tag_form_update.html')

@require_authenticated_permission( 'nutr.delete_tag')
class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    success_url = reverse_lazy(
        'nutr_tag_list')
    template_name = (
        'nutr/tag_confirm_delete.html')

@require_authenticated_permission( 'nutr.update_poc')
class POCUpdate(ObjectUpdateMixin, View):
    form_class = POCForm
    model = POC
    template_name = (
        'nutr/poc_form_update.html')

@require_authenticated_permission( 'nutr.delete_poc')
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

@require_authenticated_permission( 'nutr.delete_newslink')
class NewsLinkDelete(
        NewsLinkGetObjectMixin,
        POCContextMixin,
        DeleteView):
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'

    def get_success_url(self):
        return (self.object.poc
                .get_absolute_url())


@require_authenticated_permission( 'nutr.update_newslink')
class NewsLinkUpdate(
        NewsLinkGetObjectMixin,
        POCContextMixin,
        UpdateView):
    form_class = NewsLinkForm
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'


def upload(request):
    print('upload() (21)')
    #f request.method == 'POST' and request.FILES['myfile']:
    if request.method == 'POST':
        print('upload() (22)')
        try:
            myfile = request.FILES['myfile']
        except:
            print("Unexpected error:", sys.exc_info()[0])
        print('upload() (24)')
        fs = FileSystemStorage()
        print('upload() (26a)')
        filename = fs.save(myfile.name, myfile)
        print('upload() (26b)')
        url=fs.url(myfile.name)
        print('upload() (26d)')
        uploaded_file_url = fs.url(filename)
        print('upload() (27a) - myfile.fileno: ',str(myfile.fileno))
        #rint('upload() (27b) - myfile.seek(): ',str(myfile.seek()))
        #rint('upload() (27c) - myfile.tell(): ',str(myfile.tell()))
        print('upload() (27d) - myfile._get_name: ',str(myfile._get_name))
        print('upload() (27e) - myfile.open(): ',str(myfile.open()))
        print('upload() (27f) - myfile.read(): ',str(myfile.read()))
        print('upload() (27g) - myfile.size: ',str(myfile.size)) #222k
        print('upload() (27h) - filename: ',filename) 
        print('upload() (27i) - url: ',url) 
        #rint("upload() (27j) - form.cleaned_data['name']: ",form.cleaned_data['name'])
        print("upload() (27k) - dir(request): ",dir(request))
        #eturned=cloudinary.uploader.upload('/Users/michaelsweeney/Christmas_card.jpg')
        #eturned=cloudinary.uploader.upload(filename,use_filename=True,unique_filename=False)
        try:
            returned=cloudinary.uploader.upload(url,use_filename=True,unique_filename=False)
        except:
            print("Unexpected error:", sys.exc_info()[0])
        for k, v in returned.items():
            print ('returned dict has: ',k, v)
        """"
        returned dict has:  secure_url https://res.cloudinary.com/hh9sjfv1s/image/upload/v1503348883/whnqvmv2smbec9s8zq15.jpg
        returned dict has:  url        http://res.cloudinary.com/hh9sjfv1s/image/upload/v1503348883/whnqvmv2smbec9s8zq15.jpg
        """
        return render(request, 'nutr/poc_image_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    print('upload() (28m)')
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

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def strip_accents2(string, accents=('COMBINING ACUTE ACCENT', 'COMBINING GRAVE ACCENT', 'COMBINING TILDE')):
    accents = set(map(unicodedata.lookup, accents))
    chars = [c for c in unicodedata.normalize('NFD', string) if c not in accents]
    return unicodedata.normalize('NFC', ''.join(chars))


s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def strip_accents3(input_str):
	s = ''
	#rint input_str.encode('utf-8')
	for c in input_str:
		if c in s1:
			s += s0[s1.index(c)]
		else:
			s += c
	return s
