from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

'''

============= USUARIOS/AUTENTICAÇÃO =============

'''

def view_login(request):
    return render(request, 'registration/login.html')

def view_registro(request):

    form = RegistroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_usuario)

    context = {
        'form_registro': form
    }
    return render(request, 'registration/registro.html', context)

def list_usuario(request):
    allU = Usuario.objects.all()
    context = {
        'usuario': allU
    }

    return render(request, 'list_usuario.html', context)

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



'''

============= OBJETOS =============

'''





'''

============= EMPRESTIMO =============

'''






'''

============= RESERVA =============

'''