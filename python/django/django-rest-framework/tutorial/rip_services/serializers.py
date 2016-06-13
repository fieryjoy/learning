from rest_framework import serializers

from rip_services.models import Ripcreationrequest


class RipcreationrequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ripcreationrequest
        fields = ('archive_dataset_id', 'image_take_cat_id', 'coverage_poly',
                  'status', 'acquisition_datetime', 'cataloging_datetime',
                  'queued_datetime', 'completion_datetime', 'image_take_metadata')