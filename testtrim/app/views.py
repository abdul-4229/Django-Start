from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def book(request):
    return render(request,'book.html')
