from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewIndex, name='index'),
    path('about', ViewAbout, name='about'),
    path('create', ViewCreate, name='create'),
]
