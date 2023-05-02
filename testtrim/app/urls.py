from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fastfood', views.fastfood, name='fastfood'),
    path('brunch', views.brunch, name='brunch'),
    
]