from django.shortcuts import render
from .models import Grade, Subject

def home(request):
    grades = Grade.objects.all()
    subject =Subject.objects.all()
    return render(request, 'primary/home.html', {'grades': grades, 'subject':subject})