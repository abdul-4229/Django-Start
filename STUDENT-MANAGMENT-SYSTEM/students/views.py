from django.shortcuts import render
from .models import student

# Create your views here.
def index(request):
   
    return render(request, 'students/index.html',{
       'students': student.objects.all() 
    })