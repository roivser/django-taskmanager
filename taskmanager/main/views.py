from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def ViewIndex(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.filter(status=False).order_by('-id')
    context = {
        'title': 'Главная страница',
        'tasks': tasks
    }
    return render(request, 'main/index.html', context=context)


def ViewAbout(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/about.html')



def ViewCreate(request: HttpRequest) -> HttpResponse:
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Форма некорректна"
    form = TaskForm()
    context = {
        "form": form,
        'error': error,
    }
    return render(request, 'main/create.html', context=context)