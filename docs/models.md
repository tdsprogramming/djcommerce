# DjCommerce Models

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
The `Cart` model has the following fields:


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
The `Configuration` model allows for the ability to create different versions of products.
If you are selling shoes, you may have a `Configuration` with a `name` "size."
You can then add `ConfigurationOption`s to the `Configuration` object.
In the shoe example, you will have different sizes, so each size (9M, 7F) will be a `ConfigurationOption` instance.

## Order
```python
from djcommerce.models import Order
```
`Order` has a list of products, which is a `ManyToManyField` pointing to a `ProductInCart`.

## Products
```python
from djcommerce.models import Product
```
`Product` will be the main model

The `ProductInCart` model has two fields:
1. A `ForeignKey` that will be pointing to the Product

## Profile
```python
from djcommerce.models import Profile
```
