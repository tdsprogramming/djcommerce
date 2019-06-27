from django.db import models

from django_extensions.db.models import TimeStampedModel

from .product import ProductInCart

statuses = (
    ('complete', 'Complete'),
    ('cancelled', 'Cancelled'),
    ('shipped', 'Shipped'),
    ('returned', 'Returned'),

)

class OrderManager(models.Manager):
    def total_sold(self):
        pass
        
class Order(TimeStampedModel):
    products = models.ManyToManyField(ProductInCart)
    status = models.CharField(max_length = 50)

    def get_subtotal(self):
        return sum([p.get_subtotal for p in self.products])
