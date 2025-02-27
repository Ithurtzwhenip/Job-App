from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('',include('subscribe.urls')),
    path('uploads/',include('uploadapp.urls')),

]
