from django.urls import path
from .views import *

urlpatterns = [
    path('categorias/listar/', categoriaAPIlistar),
    path('categorias/adicionar/', categoriaAPIadicionar),
]