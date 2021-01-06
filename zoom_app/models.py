from django.db import models


class ZoomModel(models.Model):

    meeting_id = models.fields.IntegerField(null=False, blank=False, unique=True)
    participants = models.fields.IntegerField(null=False, blank=False)

    class Meta:
        db_table = "meetings"
