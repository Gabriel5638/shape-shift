from django.urls import path
from . import views

urlpatterns = [
    path('mediterranean-diet/', views.mediterranean_diet, name='mediterranean_diet'),
    path('paleo-diet/', views.paleo_diet, name='paleo_diet'),
    path('keto-diet/', views.keto_diet, name='keto_diet'),
    path('carnivore-diet/', views.carnivore_diet, name='carnivore_diet'),
    path('whole-diet/', views.whole_diet, name='whole_diet'),
]


