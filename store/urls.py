from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('men/', views.men_product_list, name='men_products'),
    path('products/women/', views.women_products, name='women_products'),
    path('keychains/', views.keychain_products, name='keychain_products'),
    path('wriststraps/', views.wriststraps_products, name='wriststraps_products'),
    path('yogamats/', views.yogamats_products, name='yogamats_products'),
    path('foamrollers/', views.foamrollers_products, name='foamrollers_products'),
    path('products/protein/', views.protein_products, name='protein_products'),
    path('creatine/', views.creatine_products, name='creatine_products'),
    path('electrolytes/', views.electrolytes_products, name='electrolytes_products'),
    path('preworkout/', views.preworkout_products, name='preworkout_products'),
    path('postworkout/', views.postworkout_products, name='postworkout_products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('all-products/', views.all_products, name='all_products'),    
]