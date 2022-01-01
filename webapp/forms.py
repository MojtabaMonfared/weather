from django import forms


class CityName(forms.Form):
    city = forms.CharField(label='City', max_length=50)
