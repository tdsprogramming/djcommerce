from django.db import models
from django.conf import settings

from localflavor.us.models import USStateField, USZipCodeField

class Address(models.Model):
    address_line_1 = models.CharField(max_length = 150)
    address_line_2 = models.CharField(max_length = 150, blank = True, null = True)
    city = models.CharField(max_length = 50)
    state = USStateField()
    zip = USZipCodeField()

    class Meta:
        abstract = False
        if settings.ADDRESS:
            abstract = True
