from django.conf import settings
from datetime import date
from django.core.urlresolvers import reverse
from django.db import models
from nutr.models import POC, Tag
from django.template.defaultfilters import slugify


# Model Field Reference
# https://docs.djangoproject.com/en/1.8/ref/models/fields/


class PostManager(models.Manager):

    def published(self):
        return self.get_queryset().filter(
            pub_date__lte=date.today())


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(
        max_length=63,
        help_text='A label for URL config',
        unique_for_month='pub_date')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='blog_posts')
    text = models.TextField()
    pub_date = models.DateField(
        'date published',
        auto_now_add=True)
    tags = models.ManyToManyField( Tag, blank=True, related_name='blog_posts', verbose_name='Country')
    pocs = models.ManyToManyField(
        POC,
        blank=True,
        related_name='blog_posts')

    objects = PostManager()
    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'
        permissions = (
            ("view_future_post",
             "Can view unpublished Post"),
        )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse(
            'blog_post_detail',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def get_archive_month_url(self):
        return reverse(
            'blog_post_archive_month',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month})

    def get_archive_year_url(self):
        return reverse(
            'blog_post_archive_year',
            kwargs={'year': self.pub_date.year})

    def get_delete_url(self):
        return reverse(
            'blog_post_delete',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})

    def get_update_url(self):
        return reverse(
            'blog_post_update',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug})
