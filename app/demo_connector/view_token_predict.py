import requests
from django.shortcuts import render
from django.template import RequestContext

from .forms import TokenPredictForm


def token_predict(request):
    if request == 'GET':
        form = TokenPredictForm()
        args = {
            "form": form
        }
    else:
        form = TokenPredictForm(request.POST)
        if form.is_valid():
            number_of_results = form.cleaned_data['forecast']

            response = requests.get(
                # Container port is needed not the "host port" from the compose
                "http://token_predict:5000/predict/?forecast={}".format(number_of_results),
                verify=False,
                params=request.GET)

            data = response.json()
            args = {
                "data": data,
                "form": form
            }
        else:
            args = {
                "form": form
            }

    return render(request, "token_predict.html", args, RequestContext(request))
