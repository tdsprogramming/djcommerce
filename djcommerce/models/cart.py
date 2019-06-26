from django.db import models

from django_extensions.db.models import TimeStampedModel

from .product import Product

class Cart(TimeStampedModel):
    products = models.ManyToManyField(Product, related_name = 'carts')
