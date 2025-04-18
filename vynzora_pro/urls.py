"""
URL configuration for vynzora_pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from vynzora_app.sitemap import StaticViewSitemap, BlogSitemap, CategorySitemap, WebsiteSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blogs': BlogSitemap,
    'categories': CategorySitemap,
    'websites': WebsiteSitemap,
}

def robots_txt(request):
    content = """
    User-agent: *
    Disallow: /admin/
    Disallow: /secret/
    Disallow: /private/
    Allow: /static/
    Sitemap: https://vynzora.com/sitemap.xml
    """
    return HttpResponse(content.strip(), content_type="text/plain")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vynzora_app.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", robots_txt),  # Added this line for serving robots.txt
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'vynzora_app.views.page_404'

