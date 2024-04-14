from django.shortcuts import render
from django.http import HttpRequest
import json
import requests


def get_air_quality(zipcode):
    """
    This function is for getting the response from the server
    Args:
        zipcode:

    Returns:

    """
    url = f'https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode}&distance=25&API_KEY=A5712589-DC70-4E5E-AC9A-5BBD81330101'

    try:
        api_get = requests.get(url)
        data = json.loads(api_get.text)
        return data
    except (requests.RequestException, json.JSONDecodeError):
        return None


def get_category_description(category_name):
    """
    This function is for getting the category description
    Args:
        category_name:

    Returns:

    """
    categories = {
        'Good': "Air quality is satisfactory, and air pollution poses little or no risk",
        'Moderate': "Air quality is acceptable. However, there may be a risk for some people, particularly those who "
                    "are unusually sensitive to air pollution.",
        'Unhealthy for Sensitive Groups': "Members of sensitive groups may experience health effects. The general "
                                          "public is less likely to be affected.",
        'Unhealthy': "Some members of the general public may experience health effects; members of sensitive groups "
                     "may experience more serious health effects.",
        'Very Unhealthy': "Health alert: The risk of health effects is increased for everyone.",
        'Hazardous': "Health warning of emergency conditions: everyone is more likely to be affected."
    }
    return categories.get(category_name, '')


def index_view(request):
    zipcode = request.POST.get('zipcode', '44473')
    print(zipcode)
    data = get_air_quality(zipcode)
    print(data)
    if not data:
        return render(request, 'lookup/home.html')
    category_name = data[0]['Category']['Name']
    category_description = get_category_description(category_name)
    category_color = category_name.lower().replace(' ', '_')

    context = {
        'data': data,
        'category_name': category_name,
        'category_description': category_description,
        'category_color': category_color
    }
    return render(request, 'lookup/home.html', context)
