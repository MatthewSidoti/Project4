from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('add-inventory/', views.add_inventory, name='add-inventory'),
    path('edit-inventory/<int:pk>/', views.edit_inventory, name='edit-inventory'),
    path('delete-inventory/<int:pk>/', views.delete_inventory, name='delete-inventory'),
    path('recipes/', views.recipes, name='recipes'),
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('login/', auth_views.LoginView.as_view(template_name='Locker_Api/login.html'), name='login'),
]