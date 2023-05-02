from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def fastfood(request):
    return render(request,'fastfood.html')
def brunch(request):
    return render(request,'brunch.html')
def staff_expenses(request):
    return render(request,'staff_expenses.html')
def service_expenses(request):
    return render(request,'service_expenses.html')