from django.shortcuts import render

from .view_token_predict import token_predict


# Create your views here.

def demo_connector(request):
    return render(request, 'demo_connector.html')


def call_token_predict(request):
    return token_predict(request)
