from django.core.urlresolvers import reverse
from django.db import models
# Model Field Reference
# https://docs.djangoproject.com/en/1.8/ref/models/fields/
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify
import unicodedata
import datetime as dt

fs=FileSystemStorage(location='images')

def generate_upload_path(instance, filename):
    return os.path.join(settings.STATIC_ROOT, 'images/')

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

class Tag(models.Model):
    name = models.CharField(
        max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text='A label for URL config.')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('nutr_tag_detail',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('nutr_tag_delete',
                       kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('nutr_tag_update',
                       kwargs={'slug': self.slug})

class POC(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    #mage=models.ImageField(upload_to=generate_upload_path, null=True, blank=True)
    image=models.ImageField(upload_to=generate_upload_path)
    #ags = models.ManyToManyField(Tag, blank=True)
    tag = models.ForeignKey(Tag, models.SET_NULL, blank=True, null=True )
    link = models.URLField(max_length=2550)
    created_date = models.DateField( 'Date Account Created')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        #  
        clone3=self.name
        clone3=clone3.lstrip().rstrip()
        clone3=clone3.replace(' ','_')
        clone3+='.jpg'
        clone3 = remove_accents(clone3)
        self.image.name = clone3
        #  
        self.created_date = dt.datetime.today()
        super(POC, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('nutr_poc_detail',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('nutr_poc_update',
                       kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('nutr_poc_delete',
                       kwargs={'slug': self.slug})

    def f(instance, filename):
        ext = filename.split('.')[-1]
        if instance.pk:
            return '{}.{}'.format(instance.pk, ext)
        else:
            pass
            # do something if pk is not there yet

    def cache(self):
        """Store image locally if we have a URL"""

        if self.url and not self.photo:
            result = urllib.urlretrieve(self.url)
            self.photo.save(
                    os.path.basename(self.url),
                    File(open(result[0], 'rb'))
                    )
            self.save()

    def get_previous(self):
        previous = POC.objects.filter(pk__lt=self.pk)
        if previous:
          return previous.last()
        #eturn False 
        return self

    def get_next(self):
        next = POC.objects.filter(pk__gt=self.pk)
        if next:
          return next.first()
        #eturn False causes error on redirect after create
        return self 

    def __str__(self):
        return self.name.title()

class NewsLink(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    #oc = models.ForeignKey(POC)
    poc = models.ForeignKey(POC, models.SET_NULL, blank=True, null=True )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsLink, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

    def __str__(self):
        return "{}: {}".format(
            self.poc, self.title)

    def get_absolute_url(self):
        return self.poc.get_absolute_url()

    def get_update_url(self):
        return reverse(
            'nutr_newslink_update',
            kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse(
            'nutr_newslink_delete',
            kwargs={'pk': self.pk})
