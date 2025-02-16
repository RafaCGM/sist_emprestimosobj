from django.urls import path
from .views import *

urlpatterns = [

    # USUARIO/AUTENTICAÇÃO
    path('login/', view_login, name='login'),
    path('registro/', view_registro, name='registro'),
    path('list_usuario/', list_usuario, name='list_usuario'),

    # CATEGORIA
    path('cad_categoria/', cad_categoria, name='cad_categoria'),
    path('categorias/', list_categoria, name='list_categoria'),

    # OBJETO
    
    # EMPRÉSTIMO

    # RESERVA


]