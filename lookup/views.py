from django.shortcuts import render
from django.http import HttpRequest


def index_view(request: HttpRequest):
    return render(request, 'lookup/home.html')
