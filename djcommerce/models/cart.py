from django.db import models

from django_extensions.db.models import TimeStampedModel

from .product import ProductInCart

class Cart(TimeStampedModel):
    products_in_cart = models.ManyToManyField(ProductInCart)

    def get_subtotal(self):
        subtotal = 0
        for p in self.products_in_cart.all():
            subtotal += p.get_subtotal()
        return subtotal

    class Meta:
        abstract = True
