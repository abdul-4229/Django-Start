from django.shortcuts import render,HttpResponse

# Create your views here.
def listBooks(request):
    return render(request, 'books.html')
   