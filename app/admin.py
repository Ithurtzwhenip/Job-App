from django.contrib import admin
from django.contrib.auth.models import User

from app.models import JobPost, Location, Author, Skills


class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','salary','date')
    list_filter = ('date','salary','expiry',)
    search_fields = ('title','description')
    search_help_text = "Write your query and hit enter"
    # fields = (('title','description'),'expiry')
    # exclude = ('title',)
    fieldsets = (
        ('Basic Information', {
         'fields':('title','description',)
        }),
        ('More Information', {
            'classes': ('collapse',),
         'fields':(('expiry','salary'),'slug',)
        }),
    )
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
