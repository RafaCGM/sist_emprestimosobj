from django.urls import path
from .views import *

urlpatterns = [
    path('cad_categoria/', cad_categoria, name='cad_categoria'),
    path('categorias/', list_categoria, name='list_categoria'),
    path('cad_usuario/', cad_usuario, name='cad_usuario'),
    path('list_usuario/', list_usuario, name='list_usuario')
]