from django import forms
from .models import Product, DrinkRecipe, Inventory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku', 'name', 'category', 'quantity', 'price']

class DrinkRecipeForm(forms.ModelForm):
    class Meta:
        model = DrinkRecipe
        fields = ['name', 'recipe_url', 'image']
        widgets = {
            'recipe_url': forms.URLInput(attrs={'placeholder': 'https://example.com/recipe'})
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'quantity', 'min_quantity']