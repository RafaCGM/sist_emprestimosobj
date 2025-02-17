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