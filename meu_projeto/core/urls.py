# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Página inicial
    path('dashboard/', views.dashboard, name='dashboard'),  # Página do dashboard
]
