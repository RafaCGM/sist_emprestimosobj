from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['matricula', 'nome', 'username', 'telefone', 'email', 'password1', 'password2']

class EditUsuarioForm(UserChangeForm):
    password = None

    class Meta:
        model = Usuario
        fields = ['matricula', 'nome', 'username', 'telefone', 'email']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','descricao']

class ObjetoForm(ModelForm):
    class Meta:
        model = Objeto
        fields = ['nome','descricao','categoria']

class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario','objeto','dataDevolucao']

    dataDevolucao = forms.DateTimeField(required=False) 

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'objeto', 'dataReserva', 'dataAtendimento']

