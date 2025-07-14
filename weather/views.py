from django.shortcuts import render, redirect, reverse
import requests
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os


def form(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = reverse("weather:forecast") + f'?city={city}'
        return redirect(url)
    return render(request, 'weather/weather.html')


@login_required
def forecast(request):
    key = os.getenv('WEATHER_API_KEY')

    if not key:
        return HttpResponse('No API Key. Configure .env file according to instruction.', status=500)
    city = request.GET.get('city') or getattr(request.user, 'city', None)

    if not city:
        return redirect('weather:form')

    params = {
        'key': key,
        'q': city
    }

    try:
        response = requests.get(
            'http://api.weatherapi.com/v1/current.json', params=params)
        response.raise_for_status()
        result = response.json()

        context = {
            'city': city,
            'temp_c': result['current']['temp_c'],
            'temp_f': result['current']['temp_f'],
            'wind_kph': result['current']['wind_kph'],
            'humidity': result['current']['humidity'],
            'condition': result['current']['condition']['text'],
            'last_updated': result['current']['last_updated'],
        }

        return render(request, 'weather/forecast.html', {'weather': context})

    except requests.RequestException as e:
        return HttpResponse(f'Error fetching weather data: {e}', status=500)

    except KeyError:
        return HttpResponse('Unexpected response format from weather API', status=500)
