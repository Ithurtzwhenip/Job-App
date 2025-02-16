from django.contrib import admin
from django.contrib.auth.models import User

from app.models import JobPost

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','salary','date')

admin.site.register(JobPost, JobAdmin)
