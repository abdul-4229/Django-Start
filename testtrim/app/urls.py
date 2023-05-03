from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fastfood', views.fastfood, name='fastfood'),
    path('brunch', views.brunch, name='brunch'),
    path('staff_expenses', views.staff_expenses, name='staff_expenses'),
    path('service_expenses', views.service_expenses, name='service_expenses'),
    path('utility_bills', views.utility_bills, name='utility_bills'),
    
]