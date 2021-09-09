import django.conf
import django.core.validators
from django.db import models


# Create your models here.


class Recipe(models.Model):
    ingredient_list = [(1, "onion"), (2, "garlic"), (3, "tomato"), (4, "oil"), (5, "salt"), (6, "flour"), (7, "rice"),
                       (8, "chiles"),(9, "cheese"), (10, "corn"), (11, "lemons"), (12, "limes"), (13, "cabbage"),
                       (14, "potato"), (15, "blueberries"), (16, "apples"), (17, "sweet potato"), (18, "avocado"),
                       (19, "beans"), (20, "peanuts"), (21, "chicken"), (22, "lamb"), (23, "goat"), (24, "turkey"),
                       (25, "deer"), (26, "pork"), (27, "beef"), (28, "tacos")]

    user = models.ForeignKey(django.conf.settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authors')
    title = models.CharField(max_length=100)
    author = models.CharField(default=None, max_length=100)
    prep_time = models.IntegerField(django.core.validators.MinValueValidator(0))
    cook_time = models.IntegerField(django.core.validators.MinValueValidator(0))
    description = models.CharField(max_length=500)
    ingredients = models.CharField(choices=ingredient_list, max_length=100)


class Cookware(models.Model):
    type_list = [(1, "Dutch Oven"), ]
    title = models.TextField(name="Name of cookware", max_length=100)
    type = models.CharField(choices=type_list, max_length=100)
