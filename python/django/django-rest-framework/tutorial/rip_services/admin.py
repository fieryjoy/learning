from django.contrib import admin

# Register your models here.
from .models import Ripcreationrequest


class RipcreationrequestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ripcreationrequest Information', {'fields':
            ['archive_dataset_id', 'image_take_cat_id', 'coverage_poly',
                  'status', 'acquisition_datetime', 'cataloging_datetime',
                  'queued_datetime', 'completion_datetime', 'image_take_metadata']}),
    ]
    list_filter = ['archive_dataset_id', 'image_take_cat_id', 'coverage_poly',
                  'status', 'acquisition_datetime', 'cataloging_datetime',
                  'queued_datetime', 'completion_datetime', 'image_take_metadata']
    list_display = ['archive_dataset_id', 'image_take_cat_id', 'coverage_poly',
                  'status', 'acquisition_datetime', 'cataloging_datetime',
                  'queued_datetime', 'completion_datetime', 'image_take_metadata']


admin.site.register(Ripcreationrequest, RipcreationrequestAdmin)