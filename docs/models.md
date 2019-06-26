# DjCommerce Models
=============

## Address
------------
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
------------

## Category
------------

## Order
------------

## Product
------------

## Profile
------------
