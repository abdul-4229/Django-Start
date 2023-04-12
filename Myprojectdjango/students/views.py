from django.shortcuts import render
from .models import Student

# Create your views here.

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all()
    })

def allstudents(request):
    return render(request, 'students/allstudents.html', {
        'students': Student.objects.all()
        }) 
