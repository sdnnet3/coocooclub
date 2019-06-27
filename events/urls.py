from django.contrib import admin
from django.urls import path
from . views import eventPage


app_name = 'events'

urlpatterns = [
    path('', eventPage, name = 'main'),
    path('<created>/', eventPage)
]
