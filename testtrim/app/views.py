from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def addstudent(request):
    return render(request,'addstudent.html')
