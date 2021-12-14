from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor_admin/', views.vendor_admin, name='vendor_admin'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit_product'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('', views.vendors, name='vendors'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),
]