from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import remove_from_cart


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
    path('store/product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('all-products/', views.all_products, name='all_products'),  
    path('contact/', views.contact_view, name='contact'),
    path('contact/sucess/', views.success_view, name='sucess'),
    path('add_comment/<int:product_id>/', views.add_comment, name='add_comment'),
    path('add_rating/<int:product_id>/', views.add_rating, name='add_rating'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('add_size/<int:product_id>/', views.add_size, name='add_size'),
    path('add_quantity/<int:product_id>/', views.add_quantity, name='add_quantity'),
    path('remove/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='cart'),
]