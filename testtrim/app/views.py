from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def book(request):
    return render(request,'book.html')

def author(request):
    return render(request,'author.html')

def sale(request):
    return render(request,'sale.html')
