from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from jobapp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('',include('subscribe.urls')),
    path('uploads/',include('uploadapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
