from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Task


def ViewIndex(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.order_by('-id')
    context = {
        'title': 'Главная страница',
        'tasks': tasks
    }
    return render(request, 'main/index.html', context=context)


def ViewAbout(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/about.html')



def ViewCreate(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/create.html')