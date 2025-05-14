from django.http import HttpResponse
from django.shortcuts import render
import requests
import os 

from weatherapp.forms import WeatherForm

API_KEY = os.environ.get('API_KEY')

# Create your views here.
def index(request):
    error = None
    form = WeatherForm()
    q = request.GET.get('city')
    print(request.GET)
    if q:
        try:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={API_KEY}')
            return render(request, 'weatherapp/index.html', {'form': form, 'q': q, 'weather_data': response.json()}) 
        except:
            error = 'Error. City not found.'
            return render(request, 'weatherapp/index.html', {'form': form, 'error': error})     
    else:
        return render(request, 'weatherapp/index.html', {'form': form})