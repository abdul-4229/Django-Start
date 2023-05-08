from django.shortcuts import render,HttpResponse

# Create your views here.
def listSaler(request):
    return render(request, 'saler.html')
   