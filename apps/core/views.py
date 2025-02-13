from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# EasterEgg que ninguém se importa: lá vai o condenado abrir mais uma view

def view_home(request):
    return render(request, 'home.html')

def view_login(request):
    return render(request, 'login.html')

def view_cadastro(request):
    return render(request, 'cadastro.html')


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