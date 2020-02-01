from django import forms


class SearchForm(forms.Form):
    number_of_results = forms.IntegerField(required=True, label="Number")
    from_date = forms.CharField(required=True, label="From")
    to_date = forms.CharField(required=True, label="To")
