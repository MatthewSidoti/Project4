from django.contrib import admin
from .models import Product, DrinkRecipe, Inventory

# Register your models here.
admin.site.register(Product)
admin.site.register(DrinkRecipe)
admin.site.register(Inventory)