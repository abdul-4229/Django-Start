from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book', views.book, name='book'),
    path('author', views.author, name='author'),
    path('sale', views.sale, name='sale'),
    
]