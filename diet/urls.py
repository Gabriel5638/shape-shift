from django.urls import path
from . import views

urlpatterns = [
path('mediterranean-diet/', views.mediterranean_diet, name='mediterranean_diet'),
]