from django.db import models

from django_extensions.db.models import TimeStampedModel

from .product import ProductInCart

STATUSES = [
    ('cancelled', 'Cancelled'),
    ('complete', 'Complete'),
    ('originated', 'Originated'),
    ('pending', 'Pending'),
    ('shipped', 'Shipped'),
]

class OrderManager(models.Manager):
    def total_revenue(self, status='Complete'):
        orders = self.filter(status=status)
        return sum([o.get_subtotal() for o in orders])

class Order(TimeStampedModel):
    products = models.ManyToManyField(ProductInCart)
    status = models.CharField(max_length = 50, choices = STATUSES)

    objects = OrderManager()

    def get_subtotal(self):
        return sum([p.get_subtotal for p in self.products])

    class Meta:
        abstract = True
