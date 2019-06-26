from django.db import models

from django_extensions.db.models import TimeStampedModel

from .category import Category

class Product(TimeStampedModel):
    name = models.CharField(max_length = 150)
    categories = models.ManyToManyField(Category, related_name='products')
    in_stock

    def __str__(self):
        return "{}".format(self.name)
