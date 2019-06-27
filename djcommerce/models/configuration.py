from django.db import models


class ConfigurationOption(models.Model):
    description = models.CharField(max_length = 50)
    add_price = models.DecimalField(max_digits = 8, decimal_places = 2)

    class Meta:
        abstract = True

class Configuration(models.Model):
    name = models.CharField(max_length = 15)
    options = models.ManyToManyField(ConfigurationOption, related_name = 'configurations')
    
    class Meta:
        abstract = True
