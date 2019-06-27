from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel

from .address import Address

class Profile(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    addresses = models.ManyToManyField(Address)

    class Meta:
        abstract = True
