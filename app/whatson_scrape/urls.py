from django.urls import path

from . import views

urlpatterns = [
    path("", views.whatson_scrape, name="whatson_scrape"),
]
