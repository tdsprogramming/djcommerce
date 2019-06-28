import importlib

from django.conf import settings

def get_address_model():
    from djcommerce.models import Address
    if hasattr(settings,"ADDRESS_MODEL"):
        return importlib.import_module(settings.ADDRESS_MODEL)
    return Address

def get_cart_model():
    from djcommerce.models import Cart
    if hasattr(settings,"CART_MODEL"):
        return importlib.import_module(settings.CART_MODEL)
    return Cart

def get_category_model():
    from djcommerce.models import Category
    if hasattr(settings,"CATEGORY_MODEL"):
        return importlib.import_module(settings.CATEGORY_MODEL)
    return Category

def get_configuration_model():
    from djcommerce.models import Configuration
    if hasattr(settings,"CONFIGURATION_MODEL"):
        return importlib.import_module(settings.CONFIGURATION_MODEL)
    return Configuration

def get_configuration_option_model():
    from djcommerce.models import ConfigurationOption
    if hasattr(settings,"CONFIGURATION_OPTION_MODEL"):
        return importlib.import_module(settings.CONFIGURATION_OPTION_MODEL)
    return ConfigurationOption

def get_order_model():
    from djcommerce.models import Order
    if hasattr(settings,"ORDER_MODEL"):
        return importlib.import_module(settings.ORDER_MODEL)
    return Order

def get_product_model():
    from djcommerce.models import Product
    if hasattr(settings,"PRODUCT_MODEL"):
        return importlib.import_module(settings.PRODUCT_MODEL)
    return Product

def get_product_in_cart_model():
    from djcommerce.models import ProductInCart
    if hasattr(settings,"PRODUCT_IN_CART_MODEL"):
        return importlib.import_module(settings.PRODUCT_IN_CART_MODEL)
    return ProductInCart

def get_profile_model():
    from djcommerce.models import Profile
    if hasattr(settings,"PROFILE_MODEL"):
        return importlib.import_module(settings.PROFILE_MODEL)
    return Profile
