from django.db import models

# Create your models here.
class Grade(models.Model):
    name = models.CharField(max_length=11)

class Student(models.Model):
    name = models.CharField(max_length=40)
    tell = models.CharField(max_length=30)
    grade = models.ForeignKey(Grade,on_delete=models.CASCADE)
