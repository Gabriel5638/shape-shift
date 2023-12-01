from django.urls import path
from .views import workout_list
from . import views

urlpatterns = [
     path('workouts/', views.workout_list, name='workout_list'),
]