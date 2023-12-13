
from django.contrib import admin
from django.urls import path, include
from shloka_daga_project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shloka_daga_project.urls')),
]
