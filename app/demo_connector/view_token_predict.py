import json

import requests
from bokeh.embed import json_item
from bokeh.plotting import figure
from django.shortcuts import render
from django.template import RequestContext

from .forms import TokenPredictForm


def create_plot(json_response):
    x = [round(i["day"], 4) for i in json_response]
    y = [round(i["prediction"], 4) for i in json_response]

    plot = figure(title="test", x_axis_label="x", y_axis_label="y", plot_width=200, plot_height=300,
                  sizing_mode='stretch_both')

    plot.line(x, y, line_width=2)

    json_plot = json_item(plot, 'plot')
    stringplot = json.dumps(json_plot)
    return stringplot


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
            plot = create_plot(data)
            args = {
                "data": data,
                "form": form,
                "plot": plot,
            }
        else:
            args = {
                "form": form
            }

    return render(request,
                  "token_predict.html", args,
                  RequestContext(request)
                  )
