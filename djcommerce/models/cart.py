from django.db import models

from django_extensions.db.models import TimeStampedModel

from .product import ProductInCart

class Cart(TimeStampedModel):
    products = models.ManyToManyField(ProductInCart)

    def get_subtotal(self):
        return sum([p.get_subtotal for p in self.products])

    class Meta:
        abstract = True
