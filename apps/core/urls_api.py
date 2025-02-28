from django.urls import path
from .views import *

urlpatterns = [
    # USUARIO API URL
    path('usuarios/listar', usuarioAPIlistar),

    # OBJETO API URL
    path('objetos/listar', objetoAPIlistar),

    # CATGORIA API URL
    path('categorias/listar/', categoriaAPIlistar),
    path('categorias/adicionar/', categoriaAPIadicionar),
    path('categorias/atualizar/<int:id>/', categoriaAPIatualizar),
    path('categorias/remover/<int:id>/', categoriaAPIremover),

]