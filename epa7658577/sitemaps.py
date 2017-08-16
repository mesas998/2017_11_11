from blog.sitemaps import PostSitemap, PostArchiveSitemap
from nutr.sitemaps import TagSitemap, POCSitemap

sitemaps = {
    'post-archives': PostArchiveSitemap,
    'posts': PostSitemap,
    'pocs': POCSitemap,
    'tags': TagSitemap,
}
