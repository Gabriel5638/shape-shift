from django.contrib import admin
from .models import Product 
from .models import Comment, Rating


@admin.register(Product)  
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'image', 'category']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'text', 'created_at']
    

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating']
