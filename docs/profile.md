#djcommerce profile

The `Profile` model is used to extend the User model. Djcommerce uses a `OneToOneField` to map a profile to a User, via the `settings.AUTH_USER_MODEL`.

If you want to use this effectively, you can set up a signal when you create a new user that will automatically create a new corresponding `Profile` model.
