from django.core.urlresolvers import reverse
from django.db import models
# Model Field Reference
# https://docs.djangoproject.com/en/1.8/ref/models/fields/
from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import slugify
import unicodedata
from django.utils import timezone
from random import randint

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

CHOICES = (
    (None, "Unknown"),
    (True, "Yes"),
    (False, "No")
)

class POC(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image=models.ImageField(upload_to=generate_upload_path)
    tag = models.ForeignKey(Tag, default=1324, blank=False, null=False, verbose_name='Country' )
    link = models.URLField(max_length=2550)
    created_date = models.DateField( default=timezone.now())
    description = models.TextField(max_length=2500)
    amnesty = models.NullBooleanField(null=True, default=False)
    hrw = models.NullBooleanField(null=True, default=False,verbose_name='HRW')
    updated_date = models.DateField( default=timezone.now())
    arrest_date = models.DateField(blank=True,null=True)
    trial_date = models.DateField(blank=True,null=True)
    charge = models.TextField(blank=True,max_length=255,null=True)
    STATUS_CHOICES = (
        ('P', 'Prisoner'),
        ('R', 'Released'),
        ('A', 'Re-arrested'),
        ('E', 'Executed'),
        ('D', 'Deceased'),
    )
    status = models.CharField(null=True,max_length=1, choices=STATUS_CHOICES)
    #udge = models.TextField(blank=True,max_length=255,null=True,verbose_name="Presiding Judge")
    #eleased_date = models.DateField(blank=True,null=True)



    def save(self, *args, **kwargs):
        print('POC model (81c)')
        self.slug = slugify(self.name+'-'+str(randint(0,1000)))
        #lone3=str(' X Yàyzz ')
        clone3= str(self.name)
        print('POC model (81j)')
        #lone3 = clone3.decode("utf-8")
        clone3+='.jpg'
        clone3
        #lone3 = remove_accents(clone3) 
        print('POC model (81m)')
        for i in range(0,len(clone3)):
            if (clone3[i]==" "):
                clone3 = clone3[:i] + "_" + clone3[i+1:]
        self.image.name=clone3
        #  
        #elf.created_date = dt.datetime.today()
        print('POC model (81q)')
        super(POC, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('nutr_poc_detail',
                       kwargs={'slug': self.slug})

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
        previous = POC.objects.filter(slug__lt=self.slug)
        if previous:
          return previous.last()
        #eturn False 
        return self

    def get_next(self):
        next = POC.objects.filter(slug__gt=self.slug)
        if next:
          return next.first()
        #eturn False causes error on redirect after create
        return self 

    def __str__(self):
        return self.name.title()

    def get_newslink_create_url(self):
        return reverse(
            'nutr_newslink_create',
            kwargs={'poc_slug': self.slug})


class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    poc = models.ForeignKey(POC)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
        unique_together = ('slug', 'poc')

    def __str__(self):
        return "{}: {}".format(
            self.poc, self.title)

    def get_absolute_url(self):
        return self.poc.get_absolute_url()

    def get_delete_url(self):
        return reverse(
            'nutr_newslink_delete',
            kwargs={
                'poc_slug': self.poc.slug,
                'newslink_slug': self.slug})

    def get_update_url(self):
        return reverse(
            'nutr_newslink_update',
            kwargs={
                'poc_slug': self.poc.slug,
                'newslink_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsLink, self).save(*args, **kwargs)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='') #subdirectory of MEDIA_ROOT
    uploaded_at = models.DateTimeField(auto_now_add=True)
