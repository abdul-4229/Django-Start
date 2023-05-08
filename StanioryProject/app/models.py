from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=270)
    tell = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)

class Book(models.Model):
    title = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    file = models.FileField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Saler(models.Model):
    name = models.CharField(max_length=10)
    telephone = models.CharField(max_length=4)
    email = models.EmailField()
    Book_name = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)

