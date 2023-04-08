from django.db import models

# Create your models here.
class student(models.Model):
    student_number = models.PositiveIntegerField
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=14)
    email = models.EmailField(max_length=40)
    feild_of_study = models.CharField(max_length=20)
    gpa = models.FloatField()

    def __str__(self) :
        return f'student: {self.first_name} {self.last_name}'