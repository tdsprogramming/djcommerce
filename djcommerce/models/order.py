from django.db import models

from django_extensions.db.models import TimeStampedModel

from .product import Product

class Order(TimeStampedModel):
    products = models.ManyToManyField(Product, related_name='orders')
