from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel

from djcommerce.utils import get_product_model
from .category import Category
from .configuration import Configuration, ConfigurationOption

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
        abstract = False
        if settings.PRODUCT_MODEL:
            abstract = True

class ProductInCart(models.Model):
    product = models.ForeignKey(get_product_model(), on_delete = models.CASCADE)
    quantity = models.IntegerField()
    configuration_options = models.ManyToManyField(ConfigurationOption)

    def get_subtotal(self):
        subtotal = self.product.price
        for c in self.configuration_options.all():
            subtotal += c.add_price
        return subtotal *= self.quantity
