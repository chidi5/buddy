from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:attribute_slug>/<slug:category_slug>/', views.category, name='category'),
    path('<slug:attribute_slug>/<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
]