from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.timezone import now
from apps.banco_dados.models import *
from apps.banco_dados.forms import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# EasterEgg que ninguém se importa: lá vai o condenado abrir mais uma view

'''
============= PÁGINAS =============
'''
def view_home(request):
    return render(request, 'home.html')

def view_perfil(request):
    return render(request, 'perfil.html')


'''
============= FUNCIONALIDADES =============
'''
def view_listar_objetos(request):
    objetos = Objeto.objects.filter(disponivel=True)
    return render(request, 'listar_disponiveis.html', {'objetos': objetos})

def view_listar_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user)
    return render(request, 'listar_emprestimos.html', {'emprestimos': emprestimos})

def view_emprestar_objeto(request, objeto_id):
    objeto = get_object_or_404(Objeto, id=objeto_id)
    if objeto.disponivel:
        Emprestimo.objects.create(objeto=objeto, usuario=request.user)
        objeto.disponivel = False
        objeto.save()
    return redirect('objetos_disponiveis')

def view_devolver_objeto(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id, usuario=request.user)
    if not emprestimo.devolvido:
        emprestimo.devolvido = True
        emprestimo.dataDevolucao = now()
        emprestimo.save()
        emprestimo.objeto.disponivel = True
        emprestimo.objeto.save()
    return redirect('listar_emprestimos')


'''
============= API =============
'''
@api_view(['GET'])
def categoriaAPIlistar(request):
    categorias = Categoria.objects.all()
    categoria_serializer = CategoriaSerializer(categorias, many=True)
    return Response(categoria_serializer.data)


'''
============= EXPRESS =============
'''

def view_remover_usuarioexpress(request):
    return render(request, 'removerexpress.html')