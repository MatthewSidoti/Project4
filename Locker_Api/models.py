from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Beer', 'Beer'),
    ('Wine', 'Wine'),
    ('Spirits', 'Spirits'),
    ('Mixers', 'Mixers'),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY, default='Spirits')
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name

class DrinkRecipe(models.Model):
    name = models.CharField(max_length=100)
    recipe_url = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    min_quantity = models.PositiveIntegerField(default=5)
    
    def __str__(self):
        return f"{self.product.name} - {self.quantity}"