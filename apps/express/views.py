from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from apps.banco_dados.models import *
from apps.banco_dados.forms import *
import requests
import json


def view_remover_usuario_express(request):
    response = requests.post("http://localhost:3000/usuarios/list")
    usuarios = json.loads(response.content)
    return render(request, "remover_express.html", { "usuarios": usuarios})

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
            '''
            se retornou usuário, deu certo a autenticação. 
            Então estou salvando na sessão o objeto json
            recebido.
            '''
            request.session['usuario'] = resposta.json()
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

    return render(request, 'registro_express.html')


def view_perfil_express(request):
    '''
    Verifica se tem a chave 'usuario' na sessão. Se tiver, 
    é pq o usuário está autenticado e poderá abrir a página
    de Perfil. Caso não exista, não abrirá Perfil e redirecionará
    o usuário para login.
    '''
    if 'usuario' in request.session.keys():
        context = {
            'nome': request.session['usuario']['nome'],
            'email': request.session['usuario']['email']
        }   
        return render(request, 'perfil.html', context)
    else:
        return redirect('login')


def desconectar(request):
    '''
    Excluir a chave 'usuario' da sessão,
    desta forma o usuário estará deslogando.
    '''
    del request.session['usuario']
    return redirect("home")
