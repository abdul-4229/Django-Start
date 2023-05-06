from django.shortcuts import render,HttpResponse

# Create your views here.
def listAuthor(request):
    return render(request, 'author.html')
   