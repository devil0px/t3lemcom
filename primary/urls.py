from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='primary_home'),
]