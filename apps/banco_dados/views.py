from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import requests
import json


'''

============= USUARIOS/AUTENTICAÇÃO =============

'''

def view_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        #user = authenticate(request, email=email, password=password)

        autenticacao = {
            'email': email,
            'password': password,
        }

        resposta = requests.post('http://localhost:3000/signin', 
                data=json.dumps(autenticacao), 
                headers={"Content-Type": "application/json"})

        if('nome' in resposta.json()):
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    
    else:
        return render(request, "registration/login.html")

    return render(request, 'registration/login.html')

def view_deslogar(request):
    logout(request)
    return redirect("login")

def view_registro(request):

    form = RegistroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(view_login)

    context = {
        'form_registro': form
    }
    return render(request, 'registration/registro.html', context)

def list_usuario(request):
    allU = Usuario.objects.all()
    context = {
        'usuario': allU
    }

    return render(request, 'list_usuarios.html', context)

def editar_registro(request, matricula):
    registro = Usuario.objects.get(pk=matricula)
    form = RegistroForm(request.POST or None, instance=registro)

    if form.is_valid():
        form.save()
        return redirect('list_usuario')
    
    context = {
        'form_registro': form
    }
    return render(request, 'registration/registro.html', context)

def remover_registro(request, matricula):
    user = Usuario.objects.get(pk=matricula)
    user.delete()
    return redirect('list_usuario')

'''

============= CATEGORIAS =============

'''

def cad_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_categoria)

    context = {
        'form_categoria': form
    }

    return render(request, 'cad_categoria.html', context)

def list_categoria(request):
    allC = Categoria.objects.all()
    context = {
        'catg': allC
    }

    return render(request, 'list_categorias.html', context)

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

def remover_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    categoria.delete()
    return redirect('list_categoria')


'''

============= OBJETOS =============

'''

def cad_objeto(request):
    form = ObjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_objeto)

    context = {
        'form_objeto': form
    }

    return render(request, 'cad_objeto.html', context)

def list_objeto(request):
    allC = Objeto.objects.all()
    context = {
        'obj': allC
    }

    return render(request, 'list_objetos.html', context)

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

def remover_objeto(request, id):
    objeto = Objeto.objects.get(pk=id)
    objeto.delete()
    return redirect('list_objeto')



'''

============= EMPRESTIMO =============

'''

def cad_emprestimo(request):
    form = EmprestimoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_emprestimo)

    context = {
        'form_emprestimo': form
    }

    return render(request, 'cad_emprestimo.html', context)

def list_emprestimo(request):
    allC = Emprestimo.objects.all()

    context = {
        'emp': allC
    }

    return render(request, 'list_emprestimos.html', context)

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

def remover_emprestimo(request, id):
    emprestimo = Emprestimo.objects.get(pk=id)
    emprestimo.delete()
    return redirect('list_emprestimo')


'''

============= RESERVA =============

'''

def cad_reserva(request):
    form = ReservaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_reserva)

    context = {
        'form_reserva': form
    }
    return render(request, 'cad_reserva.html', context)

def list_reserva(request):

    allR = Reserva.objects.all()

    context = {
        'resv': allR
    }

    return render(request, 'list_reserva.html', context)

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

def remover_reserva(request, id):
    reserva = Reserva.objects.get(pk=id)
    reserva.delete()
    return redirect('list_reserva')