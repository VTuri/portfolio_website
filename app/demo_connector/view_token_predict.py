from django.shortcuts import render


def token_predict(request):
    return render(request, "token_predict.html")
