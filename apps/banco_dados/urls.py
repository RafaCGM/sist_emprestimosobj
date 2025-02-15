from django.urls import path
from .views import *

urlpatterns = [
    path('categorias/', list_categoria, name='list_categoria'),
    path('cad_categoria/', cad_categoria, name='cad_categoria')
]