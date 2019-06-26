from django.db import models

from django_extensions.db.models import TimeStampedModel

from .cart import Cart

class Order(TimeStampedModel):
    cart = models.OneToOneField(Cart)
