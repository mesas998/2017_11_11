from django.contrib import admin

from .models import NewsLink, POC, Tag

admin.site.register(NewsLink)
admin.site.register(POC)
admin.site.register(Tag)
