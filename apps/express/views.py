from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from apps.banco_dados.models import *
from apps.banco_dados.forms import *
import requests
import json

# Create your views here.

def view_login_express(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

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
        return render(request, "login_express.html")

    return render(request, 'login_express.html')

def view_registro_express(request):
    if request.method == "POST":
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        email = request.POST['email']
        password = request.POST['password']

        usuario = {
            'nome': nome,
            'cpf': cpf,
            'telefone': telefone,
            'email': email,
            'password': password,
        }

        resposta = requests.post('http://localhost:3000/signup', 
                data=json.dumps(usuario), 
                headers={"Content-Type": "application/json"})
        
        return redirect('login_express')

    return render(request, 'registration/registro_express.html')