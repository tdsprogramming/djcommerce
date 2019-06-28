import importlib

from django.conf import settings

from djcommerce.models import (
    Address,
    Cart,
    Category,
    Configuration,
    ConfigurationOption,
    Order,
    Product,
    ProductInCart,
    Profile
)

def get_address_model():
    if settings.ADDRESS_MODEL:
        return importlib.import_module(settings.ADDRESS_MODEL)
    return Address

def get_cart_model():
    if settings.CART_MODEL:
        return importlib.import_module(settings.CART_MODEL)
    return Cart

def get_category_model():
    if settings.CATEGORY_MODEL:
        return importlib.import_module(settings.CATEGORY_MODEL)
    return Category

def get_configuration_model():
    if settings.CONFIGURATION_MODEL:
        return importlib.import_module(settings.CONFIGURATION_MODEL)
    return Configuration

def get_configuration_option_model():
    if settings.CONFIGURATION_OPTION_MODEL:
        return importlib.import_module(settings.CONFIGURATION_OPTION_MODEL)
    return ConfigurationOption

def get_order_model():
    if settings.ORDER_MODEL:
        return importlib.import_module(settings.ORDER_MODEL)
    return Order

def get_product_model():
    if settings.PRODUCT_MODEL:
        return importlib.import_module(settings.PRODUCT_MODEL)
    return Product

def get_product_in_cart_model():
    if settings.PRODUCT_IN_CART_MODEL:
        return importlib.import_module(settings.PRODUCT_IN_CART_MODEL)
    return ProductInCart

def get_profile_model():
    if settings.PROFILE_MODEL:
        return importlib.import_module(settings.PROFILE_MODEL)
    return Profile
