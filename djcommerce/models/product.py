from django.db import models

from django_extensions.db.models import TimeStampedModel

from .category import Category

class ProductManager(models.Manager):
    pass

class Product(TimeStampedModel):
    name = models.CharField(max_length = 150)
    categories = models.ManyToManyField(Category, related_name='products')
    stock = models.IntegerField(default = 0)

    def __str__(self):
        return "{}".format(self.name)

    def add_inventory(self, number = 1):
        self.stock += number
        self.save()

    def remove_inventory(self, number = 1):
        self.stock -= number
        self.save()

class ProductInCart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField
