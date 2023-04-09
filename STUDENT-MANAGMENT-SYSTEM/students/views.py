from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import student
from .forms import StudentForm


# Create your views here.
def index(request):
   
    return render(request, 'students/index.html',{
       'students': student.objects.all() 
    })


def view_student(request, id):
    student = student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_feild_of_study = form.cleaned_data['feild_of_study']
            new_gpa = form.cleaned_data['gpa']

            newstudent = student(
                student_number = new_student_number,
                first_name =   new_first_name,
                last_name = new_last_name,
                email = new_email,
                feild_of_study = new_feild_of_study,
                gpa = new_gpa
                )

            newstudent.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True,
            })
        else:
            form = StudentForm()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
            })