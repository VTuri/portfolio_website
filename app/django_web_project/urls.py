"""django_web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'

urlpatterns = [
                  path('', include('home.urls')),
                  path('admin/', admin.site.urls),
                  path('projects/', include("projects.urls")),
                  path("blog/", include("blog.urls")),
                  path('about/', include('about.urls')),
                  path('contact/', include('contact.urls')),
                  path('ckeeditor/', include('ckeditor_uploader.urls')),
                  re_path(r'^favicon\.ico$', favicon_view),
                  path("whatson_scrape/", include("whatson_scrape.urls")),
                  path("demo_connector/", include("demo_connector.urls")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
