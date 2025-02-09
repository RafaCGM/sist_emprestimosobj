from django.shortcuts import render

# Create your views here.

# EasterEgg que ninguém se importa: lá vai o condenado abrir mais uma view

def view_home(request):
    return render(request, 'home.html')

def view_login(request):
    return render(request, 'login.html')

def view_cadastro(request):
    return render(request, 'cadastro.html')