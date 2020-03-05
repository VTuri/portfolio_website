from django import forms


class TokenPredictForm(forms.Form):
    forecast = forms.IntegerField(required=True, min_value=0, max_value=100, label="Maximum number of predicted days")
