from django.urls import path
from .views import home, teacher_list


urlpatterns = [
    path('', home, name='home'),
    path('teachers/', teacher_list, name='teacher_list'),
]