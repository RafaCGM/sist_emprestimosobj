from django.urls import path
from .views import *

urlpatterns = [
    # USUARIO API URL
    path('usuarios/listar', usuarioAPIlistar),

    # CATGORIA API URL
    path('categorias/listar/', categoriaAPIlistar),
    path('categorias/adicionar/', categoriaAPIadicionar),
]