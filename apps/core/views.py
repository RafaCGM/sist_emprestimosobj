from django.shortcuts import render, redirect
from apps.banco_dados.models import Categoria
from apps.banco_dados.forms import CategoriaForm
from django.http import JsonResponse
# Create your views here.

# EasterEgg que ninguém se importa: lá vai o condenado abrir mais uma view

def view_home(request):
    return render(request, 'home.html')

def view_login(request):
    return render(request, 'login.html')

def view_cadastro(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(view_perfil)

    context = {
        'form_categoria': form
    }
    return render(request, 'cadastro.html', context)

#local onde vai ser possível ver as informações
def view_perfil(request):
    allC = Categoria.objects.all()
    context = {
        'catg': allC
    }
    return render(request, 'perfil.html', context)

def view_Json(request):
    comments = [
        {'name' : 'Prenho Souza',
        'username' : 'Lobo mau da bolsa',
        'matricula' : '20231198060010'},
        {'name' : 'Rafael',
         'username' : 'tripa seca',
        'matricula' : '20231198060020'
        },
        {'name' : 'Euller',
         'username' : 'hair and shoulders',
        'matricula' : '20231198060030'
        }
    ]

    return JsonResponse({'comments' : comments})