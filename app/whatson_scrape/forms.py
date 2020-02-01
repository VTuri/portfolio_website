from django import forms


class SearchForm(forms.Form):
    number_of_results = forms.IntegerField(required=True, label="Maximum number of results")
    from_date = forms.CharField(required=True, label="Start date (Example: 01/02/2020)")
    to_date = forms.CharField(required=True, label="End date (Example: 10/02/2020)")
