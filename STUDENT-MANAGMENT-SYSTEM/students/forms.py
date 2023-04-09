from django import forms
from .models import student


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields  = ['student_number', 'first_name', 'last_name', 'email', 'feild_of_study','gpa']
        labels = {
            'student_number' 'Student Number', 
            'first_name' 'First Name', 
            'last_name''Last Name', 
            'email' 'Email', 
            'feild_of_study' 'Feild Of Study',
            'gpa' 'GPA', 
        }

        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'feild_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }




