from django.db import models

from django_extensions.db.models import TimeStampedModel

from .category import Category
from .configuration import Configuration

class ProductManager(models.Manager):
    pass

class Product(TimeStampedModel):
    name = models.CharField(max_length = 150)
    categories = models.ManyToManyField(Category, related_name='products_in_category')
    stock = models.IntegerField(default = 0)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    configurations = models.ManyToManyField(Configuration, related_name='products_with_configuration')

    def __str__(self):
        return "{}".format(self.name)

    def add_inventory(self, number = 1):
        self.stock += number
        self.save()

    def remove_inventory(self, number = 1):
        self.stock -= number
        self.save()

    class Meta:
        abstract = True

class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField()

    def get_subtotal(self):
        return self.product.price * Decimal(self.quantity)

    class Meta:
        abstract = True
