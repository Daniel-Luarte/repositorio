from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index),
    path('pagina2/', views.saludo),
]