from django.shortcuts import render, HttpResponse, redirect

from .api import *
from .forms import CityName


def get_data_by_city(request):
    form = CityName(request.POST or None)
    if form.is_valid():
        json_data = get_current_weather(form.cleaned_data['city'])
        if 'error' in json_data:
            context = {
                'error': json_data['error']['message'],
                'wrong_name': form.data['city'],
            }
            return render(request, 'webapp/data.html', context)
        else:
            context = {
                'city': json_data['location']['name'],
                'country': json_data['location']['country'],
                'temp': json_data['current']['temp_c'],
                'temp_f': json_data['current']['temp_f'],
                'condition': json_data['current']['condition']['text'],
                'icon': json_data['current']['condition']['icon'],
                'wind_kph': json_data['current']['wind_kph'],
                'humidity': json_data['current']['humidity'],
                'lat': json_data['location']['lat'],
                'lon': json_data['location']['lon'],
                }
            # return render(request, 'webapp/data.html', context)
            return render(request, 'webapp/result.html', context)
    return render(request, 'webapp/data.html', {'form': form})