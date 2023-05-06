from django.urls import path
from app.Code import Books,Author
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book', Books.listBooks, name='book'),
    path('author', Author.listAuthor, name='author'),
    
]