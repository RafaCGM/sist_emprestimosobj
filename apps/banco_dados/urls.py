from django.urls import path
from .views import *

urlpatterns = [

    # USUARIO/AUTENTICAÇÃO
    path('login/', view_login, name='login'),
    path('registro/', view_registro, name='registro'),
    path('usuarios/', list_usuario, name='list_usuario'),
    path('editar_usuario/<int:matricula>/', editar_registro, name='edit'),
    path('remover_usuario/<int:matricula>/', remover_registro, name='remove'),

    # CATEGORIA
    path('cad_categoria/', cad_categoria, name='cad_categoria'),
    path('categorias/', list_categoria, name='list_categoria'),
    path('editar_categoria/<int:id>/', editar_categoria, name='edit_categoria'),
    path('remover_categoria/<int:id>/', remover_categoria, name='remove_categoria'),

    # OBJETO
    path('cad_objeto/', cad_objeto, name='cad_objeto'),
    path('objetos/', list_objeto, name='list_objeto'),
    path('editar_objeto/<int:id>/', editar_objeto, name='edit_objeto'),
    path('remover_objeto/<int:id>/', remover_objeto, name='remove_objeto'),

    # EMPRÉSTIMO
    path('cad_emprestimo/', cad_emprestimo, name='cad_emprestimo'),
    path('emprestimos/', list_emprestimo, name='list_emprestimo'),
    path('editar_emprestimo/<int:id>/', editar_emprestimo, name='edit_emprestimo'),
    path('remover_emprestimo/<int:id>/', remover_emprestimo, name='remove_emprestimo'),

    # RESERVA
    
    path('cad_reserva/', cad_reserva, name='cad_reserva'),
    path('reservas/', list_reserva, name='list_reserva'),
]