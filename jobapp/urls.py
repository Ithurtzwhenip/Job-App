from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Main app at root
    path('subscribe/', include('subscribe.urls')),  # Add a unique prefix
    path('uploads/', include('uploadapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
