from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
# from app.views import hello, job_detail
# from app import views
from . import views

urlpatterns = [
    path('', views.job_list, name='job_home'),
    path('job/<int:id>', views.job_detail, name='job_detail'),
]
