from django.urls import path
from django.contrib import admin
from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create_grade, name='create'),
    path('read/',views.read_grade, name='read'),
]