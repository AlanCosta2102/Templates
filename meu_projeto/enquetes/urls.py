# enquetes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_enquetes'),  # Página inicial de enquetes
]
