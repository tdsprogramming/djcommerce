from django.db import models

from django_extensions.db.models import TimeStampedModel

class Category(TimeStampedModel):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        abstract = True
