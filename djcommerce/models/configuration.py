from django.db import models


class ConfigurationOption(models.Model):
    description = models.CharField(max_length = 50)

class Configuration(models.Model):
    name = models.CharField(max_length = 15)
    options = models.ManyToManyField(ConfigurationOption, related_name = 'configurations')
