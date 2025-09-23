from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
import requests
import json

'''

============= USUARIOS/AUTENTICAÇÃO =============

'''

def view_login(request):
    if request.POST:
        email = request.POST["email"]
        senha = request.POST["password"]
        user = authenticate(request, email=email, password=senha)

        if user is not None:
            login(request, user)
            return redirect("perfil")
        else:
            return render(request, "registration/login.html")
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, 'registration/login.html')

def view_registro(request):
    form = RegistroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    contexto = {
        'form_registro': form,
        'editar': False
    }

    return render(request, 'registration/registro.html', contexto)

@login_required
def list_usuario(request):
    allU = Usuario.objects.all()
    context = {
        'usuario': allU
    }

    return render(request, 'list_usuarios.html', context)

@login_required
def editar_registro(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = EditUsuarioForm(request.POST or None, instance=usuario)

    context = {
        'form_registro': form,
        'editar': True
    }

    if form.is_valid():
        form.save()
        return redirect('list_usuario')

    return render(request, 'registration/registro.html', context)

@login_required
def remover_registro(request, id):
    user = Usuario.objects.get(pk=id)
    user.delete()
    return redirect('list_usuario')

def view_deslogar(request):
    logout(request)
    return redirect("login")



'''

============= CATEGORIAS =============

'''

@login_required
def cad_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_categoria)

    context = {
        'form_categoria': form
    }

    return render(request, 'cad_categoria.html', context)

@login_required
def list_categoria(request):
    allC = Categoria.objects.all()
    context = {
        'catg': allC
    }

    return render(request, 'list_categorias.html', context)

@login_required
def editar_categoria(request, id):
    catg = Categoria.objects.get(pk=id)
    form = CategoriaForm(request.POST or None, instance=catg)

    if form.is_valid():
        form.save()
        return redirect('list_categoria')
    
    context = {
        'form_categoria': form
    }
    return render(request, 'cad_categoria.html', context)

@login_required
def remover_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    categoria.delete()
    return redirect('list_categoria')



'''

============= OBJETOS =============

'''

@login_required
def cad_objeto(request):
    form = ObjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_objeto)

    context = {
        'form_objeto': form
    }

    return render(request, 'cad_objeto.html', context)

@login_required
def list_objeto(request):
    allC = Objeto.objects.all()
    context = {
        'obj': allC
    }

    return render(request, 'list_objetos.html', context)

@login_required
def editar_objeto(request, id):
    editarObjeto = Objeto.objects.get(pk=id)
    form = ObjetoForm(request.POST or None, instance=editarObjeto)

    if form.is_valid():
        form.save()
        return redirect('list_objeto')
    
    context = {
        'form_objeto': form
    }
    return render(request, 'cad_objeto.html', context)

@login_required
def remover_objeto(request, id):
    objeto = Objeto.objects.get(pk=id)
    objeto.delete()
    return redirect('list_objeto')



'''

============= EMPRESTIMO =============

'''

@login_required
def cad_emprestimo(request):
    form = EmprestimoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_emprestimo)

    context = {
        'form_emprestimo': form
    }

    return render(request, 'cad_emprestimo.html', context)

@login_required
def list_emprestimo(request):
    allC = Emprestimo.objects.all()

    context = {
        'emp': allC
    }

    return render(request, 'list_emprestimos.html', context)

@login_required
def editar_emprestimo(request, id):
    editarEmprestimo = Emprestimo.objects.get(pk=id)
    form = EmprestimoForm(request.POST or None, instance=editarEmprestimo)

    if form.is_valid():
        form.save()
        return redirect('list_emprestimo')
    
    context = {
        'form_emprestimo': form
    }
    return render(request, 'cad_emprestimo.html', context)

@login_required
def remover_emprestimo(request, id):
    emprestimo = Emprestimo.objects.get(pk=id)
    emprestimo.delete()
    return redirect('list_emprestimo')



'''

============= RESERVA =============

'''

@login_required
def cad_reserva(request):
    form = ReservaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_reserva)

    context = {
        'form_reserva': form
    }
    return render(request, 'cad_reserva.html', context)

@login_required
def list_reserva(request):

    allR = Reserva.objects.all()

    context = {
        'resv': allR
    }

    return render(request, 'list_reserva.html', context)

@login_required
def editar_reserva(request, id):
    editarReserva = Reserva.objects.get(pk=id)
    form = ReservaForm(request.POST or None, instance=editarReserva)

    if form.is_valid():
        form.save()
        return redirect('list_reserva')
    
    context = {
        'form_reserva': form
    }
    return render(request, 'cad_reserva.html', context)

@login_required
def remover_reserva(request, id):
    reserva = Reserva.objects.get(pk=id)
    reserva.delete()
    return redirect('list_reserva')