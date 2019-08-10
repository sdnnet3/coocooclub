from django.contrib import admin
from django.urls import path
from . views import inMemory


app_name = 'inmemory'

urlpatterns = [
    path('', inMemory, name = 'main'),
]
