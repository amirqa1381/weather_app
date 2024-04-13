from django.shortcuts import render
from django.http import HttpRequest
import json
import requests


def index_view(request: HttpRequest):
    url = 'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=75211&distance=5&API_KEY=A5712589-DC70-4E5E-AC9A-5BBD81330101'
    api_get = requests.get(url)
    data = json.loads(api_get.text)
    context = {
        'data': data
    }
    return render(request, 'lookup/home.html', context)
