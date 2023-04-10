from django.shortcuts import render,redirect
from app.models import Grade

# Create your views here.

def index(request):
    return render(request, 'index.html')


def create_grade(request):
    new_name = request.POST["name"] # waxaan qabsaday userka fasalka uu soo geliayay
    add_grade = Grade(name=new_name) # ka dib markaan waxaan ku shubay table =keyga databasekiisa
    add_grade.save() # markaana waxaan sace gareeyay hal fasal 
    return redirect('/') # markaana waxaa refresh ah kama dhacaayo page-keyga


def read_grade(request):
    allgrades = Grade.objects.all()
    context = {
        'grades': allgrades
    }
    return render(request, 'results.html', context)

    