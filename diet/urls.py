from django.urls import path
from . import views

urlpatterns = [
    path('meals/', views.meal_list, name='meal_list'),
    path('meals/new/', views.meal_create, name='meal_create'),
    path('meals/<int:pk>/delete/', views.meal_delete, name='meal_delete'),
]


