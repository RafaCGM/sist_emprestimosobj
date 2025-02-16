from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

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

============= USUARIOS =============

'''

def cad_usuario(request):

    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_usuario)

    context = {
        'form_usuario': form
    }
    return render(request, 'cad_usuario.html', context)

def list_usuario(request):
    allU = Usuario.objects.all()
    context = {
        'usuario': allU
    }

    return render(request, 'list_usuario.html', context)
'''

============= OBJETOS =============

'''





'''

============= EMPRESTIMO =============

'''






'''

============= RESERVA =============

'''