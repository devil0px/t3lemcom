from django.shortcuts import render
from .models import Grade, Subject

def home(request):
    grades = Grade.objects.all()
    return render(request, 'primary/home.html', {'grades': grades})