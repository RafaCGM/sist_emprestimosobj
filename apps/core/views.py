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

@login_required
def view_perfil(request):
    return render(request, 'perfil.html')


'''
============= FUNCIONALIDADES =============
'''
def view_listar_objetos(request):
    objetos = Objeto.objects.filter(disponivel=True)
    return render(request, 'listar_disponiveis.html', {'objetos': objetos})

@login_required
def view_listar_emprestimos(request):
    emprestimos = Emprestimo.objects.filter(usuario=request.user)
    return render(request, 'listar_emprestimos.html', {'emprestimos': emprestimos})

@login_required
def view_emprestar_objeto(request, objeto_id):
    objeto = get_object_or_404(Objeto, id=objeto_id)
    if objeto.disponivel:
        Emprestimo.objects.create(objeto=objeto, usuario=request.user)
        objeto.disponivel = False
        objeto.save()
    return redirect('objetos_disponiveis')

@login_required
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
============= EXPRESS =============
'''

def view_remover_usuarioexpress(request):
    return render(request, 'removerexpress.html')



 
'''
=========================== API VIEWS ===========================
'''



'''
============= CATEGORIA =============
'''

@api_view(['GET'])
def categoriaAPIlistar(request):
    categorias = Categoria.objects.all()
    categoria_serializer = CategoriaSerializer(categorias, many=True)
    return Response(categoria_serializer.data)

@api_view(['PUT'])
def categoriaAPIadicionar(request):
    categoria = CategoriaSerializer(data=request.data)
    if categoria.is_valid():
        categoria.save()
        return Response(categoria.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def categoriaAPIatualizar(request, id):
    categoria_bd = Categoria.objects.get(id=id)
    categoria = CategoriaSerializer(data=request.data,
                                 instance=categoria_bd)
    if categoria.is_valid():
        categoria.save()
        return Response(categoria.data, status=status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def categoriaAPIremover(request, id):
    categoria_bd = Categoria.objects.get(id=id)
    if categoria_bd:
        categoria_bd.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
