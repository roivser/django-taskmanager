from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def ViewIndex(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')


def ViewAbout(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/about.html')

