from django.db import models

from django_extensions.db.models import TimeStampedModel

from .product import ProductInCart

class Cart(TimeStampedModel):
    products = models.ManyToManyField(ProductInCart)

    def get_total(self):
        total = 0
        for p in self.products.all():
            total += p.quantity * p.product.price
        return total
