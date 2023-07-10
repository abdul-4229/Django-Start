from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    book = models.CharField(max_length=30)
    price = models.FloatField()
    
def __str__(self):
    return f'Customer: {self.first_name} {self.last_name}'
