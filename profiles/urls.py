from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]