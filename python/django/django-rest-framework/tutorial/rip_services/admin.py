from django.contrib import admin

# Register your models here.
from .models import Ripcreationrequest


class RipcreationrequestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ripcreationrequest Information', {'fields':
            ['title', 'description', 'completed']}),
    ]
    list_filter = ['title', 'completed']
    list_display = ['title', 'description', 'completed']


admin.site.register(Ripcreationrequest, RipcreationrequestAdmin)