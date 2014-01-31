from los.lo import LO
from django.forms import widgets
from rest_framework.pagination import PaginationSerializer
from rest_framework import serializers


class LOSerializer(serializers.Serializer):
    title = serializers.CharField(required=False,
                                  max_length=100)
    description = serializers.CharField(widget=widgets.Textarea,
                                        max_length=100000)
    url = serializers.URLField(max_length=20, required=False)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new lo instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.title = attrs.get('title', instance.title)
            instance.description = attrs.get('code', instance.description)
            return instance

        # Create new instance
        return LO(**attrs)


class PaginatedLOSerializer(PaginationSerializer):
    """
    Serializes page objects of user querysets.
    """
    class Meta:
        object_serializer_class = LOSerializer
