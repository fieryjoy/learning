from rest_framework import serializers

from rip_services.models import Ripcreationrequest


class RipcreationrequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ripcreationrequest
        fields = ('title', 'description', 'completed')