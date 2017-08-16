from django.contrib.sitemaps import (
    GenericSitemap, Sitemap)

from .models import POC, Tag

tag_sitemap_dict = {
    'queryset': Tag.objects.all(),
}


TagSitemap = GenericSitemap(tag_sitemap_dict)

class POCSitemap(Sitemap):

    def items(self):
        return POC.objects.all()

    def lastmod(self, poc):
        if poc.newslink_set.exists():
            return (
                poc.newslink_set.latest()
                .pub_date)
        else:
            return poc.founded_date
