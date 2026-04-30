from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog, Website, Category

class VynzoraSitemap(Sitemap):
    protocol = "https"
    
    def get_domain(self, site=None):
        return "vynzora.com"

class StaticViewSitemap(VynzoraSitemap):
    changefreq = "weekly"
    priority = 1.0

    def items(self):
        return [
            "index", "about", "portfolio", "contact", "advertising",
            "web_development", "digital_marketing", "trademark", "branding",
            "it_solutions", "privacy_and_policy", "terms_and_conditions",
            "careers", "blog"
        ]
    def location(self, item):
        return reverse(item)

class BlogSitemap(VynzoraSitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return reverse('blog_details', kwargs={'slug': obj.slug})

class WebsiteSitemap(VynzoraSitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return Website.objects.all()

    def location(self, obj):
        return reverse('website_detail', kwargs={'category_slug': obj.category.slug, 'website_slug': obj.slug})

class CategorySitemap(VynzoraSitemap):
    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('view_category')
