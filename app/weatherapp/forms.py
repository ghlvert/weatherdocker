from email.policy import default
from django import forms


class WeatherForm(forms.Form):
    city = forms.CharField(max_length=150, widget=forms.TextInput())
    scale = forms.ChoiceField(
        choices=[('K', 'K'),
                 ('C', 'C'),
                 ('F', 'F')],
        widget=forms.Select
    )
