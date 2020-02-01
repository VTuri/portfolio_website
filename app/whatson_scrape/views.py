import requests
from django.shortcuts import render


# Create your views here.

def whatson_scrape(request):
    response = requests.get("http://whatson_scrape:5000/scrape/?number=100&from=01/02/2020&to=10/02/2020", verify=False,
                            params=request.GET)
    data = response.json()
    context = {
        "data": data,
    }

    return render(request, "whatson_scrape.html", context)
