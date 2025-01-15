from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Product, DrinkRecipe, Inventory
from .forms import DrinkRecipeForm, InventoryForm
from django.contrib.auth.forms import UserCreationForm

def is_owner(user):
    return user.is_authenticated and user.is_superuser

def home(request):
    return render(request, 'Locker_Api/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Locker_Api/register.html', {'form': form})

@login_required
def dashboard(request):
    inventory_count = Inventory.objects.count()
    low_stock_count = Inventory.objects.filter(quantity__lte=5).count()
    
    # Get recent activities
    recent_activities = []
    
    # Recent inventory changes
    recent_inventory = Inventory.objects.all().order_by('-last_updated')[:5]
    for item in recent_inventory:
        recent_activities.append(f"Inventory updated for {item.product.name}: {item.quantity} units")
    
    # Recent recipes
    recent_recipes = DrinkRecipe.objects.all().order_by('-created_at')[:5]
    for recipe in recent_recipes:
        recent_activities.append(f"Recipe added: {recipe.name}")

    context = {
        'inventory_count': inventory_count,
        'low_stock_count': low_stock_count,
        'recent_activities': recent_activities,
    }
    return render(request, 'Locker_Api/dashboard.html', context)

@login_required
def inventory(request):
    inventory_items = Inventory.objects.all()
    return render(request, 'Locker_Api/inventory.html', {'inventory': inventory_items})

@login_required
@user_passes_test(is_owner)
def add_inventory(request):
    if request.method == 'POST':
        sku = request.POST.get('sku')
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        
        product = Product.objects.create(
            sku=sku,
            name=name,
            category=category
        )
        
        inventory_item = Inventory.objects.create(
            product=product,
            quantity=quantity
        )
        
        messages.success(request, 'Item added successfully!')
        return redirect('inventory')
        
    return render(request, 'Locker_Api/add_inventory.html')

@login_required
@user_passes_test(is_owner)
def edit_inventory(request, pk):
    inventory_item = get_object_or_404(Inventory, pk=pk)
    
    if request.method == 'POST':
        sku = request.POST.get('sku')
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        
        inventory_item.product.sku = sku
        inventory_item.product.name = name
        inventory_item.product.category = category
        inventory_item.product.save()
        
        inventory_item.quantity = quantity
        inventory_item.save()
        
        messages.success(request, 'Item updated successfully!')
        return redirect('inventory')
        
    context = {
        'item': inventory_item
    }
    return render(request, 'Locker_Api/edit_inventory.html', context)

@login_required
@user_passes_test(is_owner)
def delete_inventory(request, pk):
    inventory_item = get_object_or_404(Inventory, pk=pk)
    
    if request.method == 'POST':
        inventory_item.product.delete()
        messages.success(request, 'Item deleted successfully!')
        return redirect('inventory')
        
    context = {
        'item': inventory_item
    }
    return render(request, 'Locker_Api/delete_inventory.html', context)

@login_required
def recipes(request):
    recipes = DrinkRecipe.objects.all()
    return render(request, 'Locker_Api/recipes.html', {'recipes': recipes})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = DrinkRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            messages.success(request, 'Recipe added successfully!')
            return redirect('recipes')
    else:
        form = DrinkRecipeForm()
    return render(request, 'Locker_Api/add_recipe.html', {'form': form})