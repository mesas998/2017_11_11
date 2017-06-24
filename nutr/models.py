from django.core.urlresolvers import reverse
from django.db import models
# Model Field Reference
# https://docs.djangoproject.com/en/1.8/ref/models/fields/
from django.core.files.storage import FileSystemStorage

fs=FileSystemStorage(location='images')

def generate_upload_path(instance, filename):
    return os.path.join(settings.STATIC_ROOT, 'images/')

class POC(models.Model):
    slug = models.SlugField(max_length=63)
    name = models.CharField(max_length=63)
    image=models.ImageField(upload_to=generate_upload_path)

    def get_absolute_url(self):
        return reverse('nutr_poc_detail',
                       kwargs={'pk': self.pk})
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
    """
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1]
            # get filename
            if instance.pk:
                filename = '{}.{}'.format(instance.pk, ext)
            else:
                # set filename as random string
                filename = '{}.{}'.format(uuid4().hex, ext)
            # return the whole path to the file
            return os.path.join(path, filename)
        return wrapper
    """


class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    poc = models.ForeignKey(POC)



class Tag(models.Model):
    name = models.CharField(
        max_length=31, unique=True)
    slug = models.SlugField(
        max_length=31,
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

