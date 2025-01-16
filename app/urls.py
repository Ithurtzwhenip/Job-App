from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from app.views import hello

urlpatterns = [
    path('',hello)
]