from django.shortcuts import render
#from .models import Grade
from .models import Teacher, Class

def home(request):
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'teachers': teachers})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'home/teacher_list.html', {'teachers': teachers})
#def homee(request):
    #grades = Grade.objects.all()  # جلب جميع الصفوف الدراسية
    #return render(request, 'home.html', {'grades': grades})