import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = 'ae74493988b0eb6f329e392f929a92ca'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    all_cities = []
    cities = City.objects.all()
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
