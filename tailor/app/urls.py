from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('local', views.local, name='local'),
    path('size', views.size, name='size'),
    
    
]