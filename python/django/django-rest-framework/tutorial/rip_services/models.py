from django.contrib.gis.db import models
from jsonfield import JSONField


TASK_STATUS = (
    ('QU', 'Queued'),
    ('RU', 'Running'),
    ('CO', 'Completed'),
    ('FA', 'Failed'),
    ('RE', 'To be retried'),
)


class Ripcreationrequest(models.Model):
    archive_dataset_id = models.IntegerField(blank=False, null=False)
    # FIXME check if cat_id is really an Integer
    image_take_cat_id = models.IntegerField(blank=False, null=False)

    coverage_poly = models.GeometryField(srid=4326, blank=True, null=True)
    status = models.CharField(
                max_length=2,
                choices=TASK_STATUS,
                default='QU')
    acquisition_datetime = models.DateTimeField(blank=False, null=False)
    cataloging_datetime = models.DateTimeField(blank=False, null=False)
    queued_datetime = models.DateTimeField(auto_now_add=False)
    completion_datetime = models.DateTimeField(blank=True, null=True)
    # FIXME should satellite be in the metadata or in a different field?
    image_take_metadata = JSONField(blank=True, null=True)

    class Meta:
        unique_together = (("archive_dataset_id", "image_take_metadata"),)