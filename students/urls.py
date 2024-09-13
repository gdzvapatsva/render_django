from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='students-home'),
    path('about/', views.about, name='students-about'),
]
