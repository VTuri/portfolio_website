from django.shortcuts import render


def token_predict(request):
    # if request == 'GET':
    #     form = SearchForm()
    #     args = {
    #         "form": form
    #     }
    # else:
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         number_of_results = form.cleaned_data['number_of_results']
    #         from_date = form.cleaned_data['from_date']
    #         to_date = form.cleaned_data['to_date']
    #
    #         response = requests.get(
    #             # Container port is needed not the "host port" from the compose
    #             "http://whatson_scraper:5000/scrape/?number={}&from={}&to={}".format(number_of_results, from_date,
    #                                                                                  to_date),
    #             verify=False,
    #             params=request.GET)
    #
    #         data = response.json()
    #         args = {
    #             "data": data,
    #             "form": form
    #         }
    #     else:
    #         args = {
    #             "form": form
    #         }

    return render(request, "token_predict.html",
                  # args, RequestContext(request)
                  )
