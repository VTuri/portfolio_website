from django.urls import path

from . import views

urlpatterns = [
    path("", views.call_token_predict, name="token_predict"),
]
