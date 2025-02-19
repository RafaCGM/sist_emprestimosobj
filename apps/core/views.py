from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# EasterEgg que ninguém se importa: lá vai o condenado abrir mais uma view

@login_required
def view_home(request):
    return render(request, 'home.html')

@login_required
def view_perfil(request):
    return render(request, 'perfil.html')

'''
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
'''