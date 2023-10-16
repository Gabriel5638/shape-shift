from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('men/', views.men_product_list, name='men_products'),
    path('products/women/', views.women_products, name='women_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('all-products/', views.all_products, name='all_products'),  # Updated URL pattern
]