from django.urls import path
from . import views

app_name = 'workouts'  

urlpatterns = [
    path('push/', views.push, name='push'),
    path('volume/', views.volume, name='volume'),
    path('texas/', views.texas, name='texas'),
    path('juggernaut/', views.juggernaut, name='juggernaut'),
    path('stronglifts/', views.stronglifts, name='stronglifts'),
]