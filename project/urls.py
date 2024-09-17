from django.urls import path, include
from django.contrib import admin


urlpatterns = [
      # هذا هو الرابط الرئيسي
    path('admin/', admin.site.urls),
    path('primary/', include('primary.urls')),
    path('secondary/', include('secondary.urls')),
    path('highschool/', include('highschool.urls')),
]