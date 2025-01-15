from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Locker_Api import views as locker_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', locker_views.home, name='home'),
    path('dashboard/', locker_views.dashboard, name='dashboard'),
    path('inventory/', locker_views.inventory, name='inventory'),
    path('add-inventory/', locker_views.add_inventory, name='add-inventory'),
    path('edit-inventory/<int:pk>/', locker_views.edit_inventory, name='edit-inventory'),
    path('delete-inventory/<int:pk>/', locker_views.delete_inventory, name='delete-inventory'),
    path('recipes/', locker_views.recipes, name='recipes'),
    path('add-recipe/', locker_views.add_recipe, name='add-recipe'),
    path('login/', auth_views.LoginView.as_view(template_name='Locker_Api/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Locker_Api/logout.html'), name='logout'),
    path('register/', locker_views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)