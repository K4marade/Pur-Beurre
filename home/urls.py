from django.urls import path
from . import views

urlpatterns = [
    path('legal/', views.legal, name='home-legal'),
    path('', views.home, name='home-home'),
]
