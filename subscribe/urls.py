from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),  # subscribe/ (default page)
    path('thank_you/', views.thank_you, name='thank_you'),  # subscribe/thank_you/
]
