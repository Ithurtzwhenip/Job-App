from django.contrib import admin
from django.contrib.auth.models import User

from app.models import JobPost

# Register your models here.

admin.site.register(JobPost)
