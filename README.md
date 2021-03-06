# DjCommerce Models
## Installation
1. `pip install djcommerce`
2. Add `djcommerce` to `INSTALLED_APPS`
    ```python
    INSTALLED_APPS = (
        ...
        'djcommerce',
        ...
    )
    ```

When you are referencing a model, we suggest you use the methods from `djcommerce.utils`. For example, if you are setting a `ForeignKey` to `Address`, please set `Address = get_address_model()`.

If you want to use the built in models, you do not need to do much configuration. However, if you want to inherit from the built in models, you need to create your own model, then in `settings.py` define where your new model is via a string.

For example, let's say you have an address app with a custom address model in `address/models.py`:

```python
from djcommerce.models import Address

class MyCustomAddress(Address):
    some_custom_field = models.CharField(max_length = 50)
```

In your `settings.py`, you will then need to make a new variable `ADDRESS_MODEL = 'address.models.MyCustomAddress'` so that it knows where to grab the address model for related models.

## Address
```python
from djcommerce.models import Address
```

The `Address` model has the following fields:
1. `address_line_1`: This will hold the street number, name as well as suffixes and prefixes.
2. `address_line_2`: A nullable field for suite or unit number
3. `city`
4. `state`: A `USStateField` from `django-localflavor`
5. `zip`: A `USZipCodeField` from `django-localflavor`

## Cart
```python
from djcommerce.models import Cart
```
The `Cart` model has a `products_in_cart` field, which is a `ManyToManyField`, pointing to the `ProductInCart` model.
You can inherit and create a new `Cart` model, if the following conditions are met:
1. The `products_in_cart` field must be a `ManyToManyField`
2. The object that the `ManyToManyField` is pointing to must have a `get_subtotal` method, in order to be able to calculate the subtotal of the cart. Or, you can just avoid this by writing your own `get_subtotal` method on the `Cart` object.

## Category
```python
from djcommerce.models import Category
```
`Category` model allows for certain products to be listed under a certain category.
For example, if you are selling clothes, you may have a category of "shirts."
You would then create a `Category` with a `description` of "shirts."

## Configuration
```python
from djcommerce.models import Configuration
```
The `Configuration` model allows for the ability to create different versions of products, with the following fields:
1. `name`: For example, size or color.
2. `options`: A `ManyToManyField` that points to `ConfigurationOption`. If the name of the `Configuration` is "size", then the `options` could be 9M, 10M, 7F, 8F, etc.


The `ConfigurationOption` model allows for options to the configuration with the following fields:
1. `description`: The description of the option (for example, "9M", "10M", "7F" "8F").
2. `add_price`: The additional price to the `price` of the corresponding `Product` object.

## Order
```python
from djcommerce.models import Order
```
1. `Order` has a list of products, which is a `ManyToManyField` pointing to a `ProductInCart`.
2. `status`: The status of which stage of the order process the users order is in.
3. `get_subtotal`: Returns the subtotal of all of the products prices in the order combined.

## Products
```python
from djcommerce.models import Product
```
`Product` will be the main model that holds your ECommerce site's products, with the following fields:
1. `name`
2. `categories`: A `ManyToManyField` that points to the `Category` model
3. `stock`: An `IntegerField` that holds how many products you have in your inventory
4. `price`: The base price for the product.
5. `configurations`: These will hold the different possible configurations. For example, color, size, etc.

The `ProductInCart` model has two fields:
1. `product`: A `ForeignKey` that will be pointing to the Product.
2. `configuration_options`: A `ManyToManyField` that is connected to the `ConfigurationOption` object. This will allow for different configurations of a product in the same cart. For example, you may have a shoe product that has different sizes and colors. The `configuration_options` field will allow for a red shoe that is size 12 to be a different `ProductInCart` instance than a blue shoe that is size 12.

## Profile
```python
from djcommerce.models import Profile
```
The `Profile` model is used to extend the User model. Djcommerce uses a `OneToOneField` to map a profile to a User, via the `settings.AUTH_USER_MODEL`.

If you want to use this effectively, you can set up a signal when you create a new user that will automatically create a new corresponding `Profile` model.
