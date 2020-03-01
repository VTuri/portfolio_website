from django.urls import path

from . import views

urlpatterns = [
    path("", views.demo_connector, name="demo_connector"),
    path("token_predict", views.call_token_predict, name="token_predict"),

]
