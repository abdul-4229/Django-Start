from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def local(request):
    return render(request,'local.html')

def size(request):
    return render(request,'size.html')


