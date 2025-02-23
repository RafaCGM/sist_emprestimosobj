from django.urls import path, include
from .views import *

urlpatterns = [

    # PRINCIPAL
    path('', view_home, name='home'),
    path('perfil/', view_perfil, name='perfil'),
    path('objetosdp/', view_listar_objetos, name='objetos_disponiveis'),
    path('emprestar/<int:objeto_id>/', view_emprestar_objeto, name='emprestar_objeto'),
    path('devolver/<int:emprestimo_id>/', view_devolver_objeto, name='devolver_objeto'),
    path('emprestimosand/', view_listar_emprestimos, name='listar_emprestimos'),
    path('removerexpress/', view_remover_usuarioexpress, name='remove_express'),

]